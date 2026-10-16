# 阶段 04 教师资料

## 目标

让学生理解从本地手动运行到自动检查、再到检查通过后部署的完整路径。部署平台使用 Railway；教师需提前确认课程账号、服务数量、持久化卷和用量预算。

## 运行环境准备

- 学生本机安装 Docker Desktop 或 Docker Engine/Compose，用于本地组合运行。
- Railway 不直接运行 Compose；提前演练如何将 `web`、`api` 两个 Compose 服务分别配置成 Railway 服务，并设置私有网络、公网域名和 API 持久化卷。
- 任务使用 GitHub Actions 做托管 CI；GitHub Actions 不是开源软件。Railway 可启用 **Wait for CI**，让 GitHub Actions 检查成功后再自动部署。
- Railway 是托管平台而非开源组件；检查可用套餐资源、卷限制、部署服务数和账单告警。为学生提供受控项目或教师演示项目，并避免共享写权限导致互相覆盖。
- 教学环境不要放真实客户数据或敏感信息。确保每个学生的 API 数据卷相互隔离。

## 关键教学点

- **CI**：自动构建和检查，失败即停止流水线。
- **CD**：将通过检查的版本交付或部署；生产环境可以要求人工审批。
- Railway 的 `web` 服务对外提供域名，`api` 服务只通过私有网络访问。
- 每个学生 API 服务的 SQLite 卷单独挂载到 `/data`，环境变量 `DATABASE_PATH` 指向卷内文件。
- 前端通过 Nginx 将 `/api` 转发到 API，避免在公网暴露额外 API 服务或引入跨域配置。
- CI 工作流应在 `main` 推送时运行；`Wait for CI` 应在所有需要自动部署的服务上开启。
