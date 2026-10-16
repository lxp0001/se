# 任务 04-3：Railway 持续部署

CI 已能检查前端与容器构建。本阶段的工作流还没有运行 Python API 行为测试；阶段 05 会把 pytest 接入同一条 CI 工作流。届时 Railway 的 **Wait for CI** 会等待新增的 API 测试也通过，再部署新版本。本任务使用 Railway 部署阶段 03 的 React 页面和阶段 02 的 FastAPI API：先手动确认服务可用，再开启自动部署。

## 完成后你应该能够

- 区分 CI 自动检查与 CD 部署。
- 将本地 Compose 中的服务映射为 Railway 服务。
- 查看 Railway 构建日志、部署状态和运行日志。
- 解释为什么数据库要挂载持久化卷，为什么不应将密钥写入仓库。

## 开始前

- 完成 04-1 和 04-2；GitHub 仓库的 `main` 分支上已有能成功运行的 CI 工作流。
- Railway 项目从同一个 GitHub 仓库创建两个服务：`api` 与 `web`。Railway 不会直接运行 Compose 文件；Compose 用于本地运行，部署时每个服务要分别连接仓库并配置根目录、变量、网络和数据卷。[Railway 的 Compose 部署说明](https://docs.railway.com/guides/docker-compose)
- 学生使用教师安排的 Railway 账号或项目；不要自行升级付费方案。Railway 的套餐和资源用量会影响费用，操作前阅读[当前价格](https://docs.railway.com/pricing/plans)。

## 第一步：部署 API 服务

1. 在 Railway 新建空项目，并添加来自 GitHub 仓库的服务，命名为 `api`。
2. 将服务根目录设为 `/stage-04/04-1-Docker打包与本地运行/starter/app/backend`，让 Railway 使用其中的 Dockerfile 构建。
3. 在 Variables 中设置 `DATABASE_PATH=/data/registrations.db`。
4. 在服务的 Volumes 中添加持久化卷，挂载路径填写 `/data`。
5. API 只供项目内服务访问，不生成公网域名。确认 FastAPI 在容器内监听 `0.0.0.0:8000`。

## 第二步：部署前端服务

1. 添加另一个来自同一 GitHub 仓库的服务，命名为 `web`，根目录设为 `/stage-04/04-1-Docker打包与本地运行/starter/app/frontend`。
2. 在 Variables 中设置 `API_ORIGIN=http://api.railway.internal:8000`。Nginx 配置会把网页发来的 `/api/` 请求转发给项目内的 API 服务。
3. 为 `web` 服务生成公网域名；不要为 API 服务开放公网入口。
4. 访问网页，完成查看活动和报名记录的 CRUD 验证；查看两个服务的部署日志。

Railway 项目中的服务可通过私有网络互相访问；要使用实际服务名和应用监听端口。参考 [Railway 私有网络与 Compose 服务映射](https://docs.railway.com/guides/docker-compose)。

## 如果前端部署在 GitHub Pages

GitHub Pages 是静态站点，不能通过 Railway 私有网络访问 `api`。如果使用 `.github/workflows/04-1-pages.yml` 部署前端，需要让 API 可通过 HTTPS 公网域名访问，并限制跨域来源：

1. 在 `api` 服务的 Variables 中设置 `CORS_ORIGINS=https://<GitHub 用户名>.github.io`，将占位内容替换为实际 Pages 域名的用户名。API 只允许配置的 Pages 来源跨域请求；不要把仓库路径（例如 `/se/`）写入来源。
2. 在 `api` 服务的 Settings → Networking → Public Networking 中选择 **Generate Domain**，记录 Railway 分配的 HTTPS 域名。API 因此可以从公网访问；不要在 API 中放置密钥或管理接口。
3. 前端 Pages 构建当前默认使用课程示例域名 `https://se-production-2cc7.up.railway.app`。如果复制仓库后使用了自己的 API 域名，在对应 GitHub 仓库 **Settings → Secrets and variables → Actions → Variables** 中设置 `VITE_API_BASE_URL`，值填自己的 HTTPS 域名，不要在域名末尾添加 `/`。Pages 地址和仓库名的关系见[GitHub Pages 前端部署说明](../GitHub-Pages前端部署.md)。
4. 重新运行 **部署前端到 GitHub Pages** 工作流。
5. 用 `https://<API 域名>/events` 检查 API 是否可访问，再从 Pages 页面测试报名功能。

如需后续将 API 改为私有网络服务，需要将前端改为 Railway 上的 `web` 服务，并由 Nginx 通过 `API_ORIGIN` 转发请求；GitHub Pages 无法连接 Railway 私有域名。

## 第三步：设置“先 CI，后部署”

每个服务都连接 GitHub 的 `main` 分支。在 Railway 服务设置中启用自动部署，并打开 **Wait for CI**。这个选项会等待该提交对应的 GitHub Actions 工作流结束：检查失败时跳过部署，检查成功后才继续部署。[Railway GitHub 自动部署说明](https://docs.railway.com/deployments/github-autodeploys)

本任务使用 Railway 与 GitHub 的原生集成，不需要自己编写 Webhook，也不需要把 Railway token 放入 Actions Secrets。只在 Railway 的服务 Variables 中填写 `DATABASE_PATH`、`API_ORIGIN` 等应用配置；这些不是要提交到 Git 仓库的文件。

## 第四步：验证持续部署

1. 修改页面上的一处安全文字并推送到 `main`。
2. 先在 GitHub Actions 页面确认构建检查成功。
3. 在 Railway 的 Deployments 页面确认新提交随后开始部署，并查看日志。
4. 打开网页确认新文字生效，新增一条 `user1` 或 `user2` 报名，再重新部署或重启 API，确认数据仍保存在 `/data` 卷中。
5. 在测试副本中制造一个构建错误并推送，确认 Actions 失败且 Railway 不部署失败版本；随后撤销错误并恢复成功。

## 费用与安全

- Railway 是托管服务，不是开源组件；套餐有资源限制，超出额度可能收费。遵循教师的账号和预算安排，部署后按要求停止或删除测试服务。
- 不提交 `.env`、密码、API token、数据库文件或私钥。Railway Variables 只填写运行所需值；不要把真实变量复制到任务总结或截图中。
- `DATABASE_PATH` 指向持久化卷中的文件。仅把数据库写在容器临时文件系统里，重新部署后数据可能丢失。

## 提交内容

```text
Railway 项目与服务配置说明（不含变量值）
.github/workflows/ci.yml
任务总结.md
```

## 完成检查

- [ ] 若前端也部署在 Railway，`web` 有公网域名且 `api` 只通过私有网络访问；若前端部署在 GitHub Pages，则 API 有公网域名并配置了精确的 `CORS_ORIGINS`。
- [ ] 前端可以读取并管理报名记录，API 数据库挂载到 `/data` 持久化卷。
- [ ] GitHub Actions 检查成功后 Railway 才部署；检查失败时不会部署失败版本。
- [ ] 能在 Railway 中找到对应提交的部署记录与日志。
- [ ] 未提交 `.env`、数据库文件、密钥或 Railway token。
