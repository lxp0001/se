# 阶段 04：容器化、持续集成与部署

本阶段把阶段 03 的 React 页面和阶段 02 的 FastAPI API 组合成一个可部署应用。学生先在本机用 Docker Compose 手动运行，再用 GitHub Actions 自动构建检查，最后让 Railway 等 CI 成功后自动部署前后端服务。

| 编号 | 任务 | 先想一想 | 学生做出的东西 | 提交内容 |
| --- | --- | --- | --- | --- |
| 04-1 | [Docker 打包与本地运行](04-1-Docker打包与本地运行/README.md) | 换一台电脑时，怎样让前端、API 和数据库按相同方式运行？ | Dockerfile、Compose 配置和可本地访问的应用 | 部署配置、必要源码修改、`任务总结.md` |
| 04-2 | [GitHub Actions 自动检查](04-2-GitHubActions自动检查/README.md) | 怎样在每次提交后自动发现构建失败？ | 自动检查前端构建与容器配置的工作流 | `.github/workflows/`、检查结果、`任务总结.md` |
| 04-3 | [Railway 持续部署](04-3-Railway持续部署/README.md) | 怎样让 Railway 等自动检查通过后再部署新版本？ | Railway 上的前后端服务、持久化数据卷和通过 CI 门控的自动部署 | Railway 配置、工作流、部署记录、`任务总结.md` |

## CI/CD 在本阶段的意思

- **CI（持续集成）**：提交代码后自动构建并运行检查。阶段 04 先检查 React 生产构建、Compose 配置和容器镜像构建；后端 Python 依赖会在镜像构建时安装，但此时还没有运行 API 行为测试。阶段 05 再加入 pytest 测试，并扩展同一条 CI 工作流。
- **CD（持续交付/部署）**：检查通过后，把版本交付或部署到环境。本阶段先手动验证一次，再让 Railway 等待 GitHub Actions 检查成功后自动部署到教学演示环境。
- 生产环境可以增加人工审批；本阶段不要求学生自动发布到真实生产服务。

## 组件选择与费用边界

- Docker Engine、Docker Compose 和 Nginx 用于本地打包与运行；Railway 负责托管和部署。
- GitHub Actions 用作托管 CI 服务；工作流配置可以查看和修改，但 Actions 服务本身不是开源软件。
- Railway 是托管平台，不是开源组件；免费方案资源有限，超出用量可能产生费用，按课程统一安排账号和预算。
- 阶段 04 不提交密钥、`.env`、数据库文件、`node_modules` 或容器镜像。

## 学习顺序

本地 Compose 可运行 → Actions 检查前端构建与镜像 → 阶段 05 加入 API 测试 → Railway 等全部 CI 检查通过后部署 → 查看在线应用与部署日志。

部署失败或前后端联调遇到问题时，参阅[阶段 04 故障排查手册](故障排查手册.md)。

如需分开部署前后端，可按这两份说明操作：[GitHub Pages 前端部署](GitHub-Pages前端部署.md)和[Railway 后端部署](Railway后端部署.md)。

Railway 不会直接运行 Compose 文件；本地 Compose 用于开发验证，部署时把 Compose 中的前端、API 服务分别配置为 Railway 服务。[Railway 的 Compose 部署说明](https://docs.railway.com/guides/docker-compose)

参考：[Docker Compose 官方入门](https://docs.docker.com/compose/gettingstarted/)、[GitHub Actions 官方文档](https://docs.github.com/actions)、[Railway GitHub 自动部署与 Wait for CI](https://docs.railway.com/deployments/github-autodeploys)。
