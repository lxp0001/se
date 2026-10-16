# 任务 04-2：GitHub Actions 自动检查

上一个任务能在本机启动完整应用。本任务把关键构建步骤放进 GitHub Actions：每次推送到个人仓库 `main` 后，自动安装前端依赖、构建 React 页面，并验证 Compose 配置和容器镜像能否构建。

## 完成后你应该能够

- 找到 GitHub Actions 工作流文件。
- 解释工作流何时启动、执行哪些检查、成功或失败在哪里查看。
- 让失败的构建阻止后续部署。

## 第一步：准备工作流

将阶段 00 的任务总结模板复制为 `任务总结.md`，在仓库 `.github/workflows/` 下新建 `ci.yml`。根据仓库中的实际目录配置步骤：

1. 检出仓库代码。
2. 设置 Node.js，在前端目录执行 `npm ci` 和 `npm run build`。
3. 安装 Docker Buildx（如构建环境需要），运行 `docker compose -f app/compose.yaml config --quiet` 检查 Compose 配置，再构建两个服务镜像。
4. 仅在上述步骤都成功后将工作流标记成功。

工作流在推送到 `main` 时运行。可参考 [GitHub Actions 快速入门](https://docs.github.com/actions/get-started/quickstart) 和 Docker 官方 Compose 文档。不要把 Actions 版本或密钥从陌生示例中盲目复制；使用课程提供或官方维护的 Actions。

## 第二步：观察成功和失败

提交并推送工作流，打开仓库的 **Actions** 页面查看运行记录。确认成功后，在测试副本中故意把前端构建脚本名改错，观察工作流失败；修复后再次提交，确认恢复成功。测试结束后不要保留故意制造的错误。

## 安全要求

- CI 构建本身不需要 Railway token，因此本任务不新增仓库 Secret。
- 不将 `.env`、密码、API token 或部署凭据写入工作流文件或提交到仓库。
- 不提交 `node_modules`、SQLite 数据库或构建缓存。

## 提交内容

```text
.github/workflows/ci.yml
任务总结.md
```

```powershell
git status
git add .github/workflows/ci.yml 任务总结.md
git commit -m "Add automated build checks"
git push origin main
```

## 完成检查

- [ ] 推送到 `main` 会自动触发工作流。
- [ ] React 构建和 Docker Compose 构建均成功。
- [ ] 故意制造构建错误时工作流失败，修复后恢复成功。
- [ ] 仓库没有密钥、`.env`、数据库文件或 `node_modules`。
