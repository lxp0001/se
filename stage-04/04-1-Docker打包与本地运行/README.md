# 任务 04-1：Docker 打包与本地运行

完成阶段 02 的 FastAPI API 和阶段 03 的 React 页面后，把它们组合成一个可重复运行的应用。先在自己电脑上手动启动 Compose；本任务不要求上传镜像或部署到公网。

## 完成后你应该能够

- 说明镜像像应用的打包模板、容器像运行中的实例。
- 使用 Docker Compose 一起启动前端和 API。
- 说明 SQLite 数据为什么要放在持久化卷中，而不能只留在容器临时文件里。

## 开始前

安装 Docker Desktop（Windows/macOS）或 Docker Engine 与 Compose 插件（Linux）。确认 Docker 正在运行。将已完成的 React 项目放入 `app/frontend`，FastAPI 项目放入 `app/backend`，然后把本目录 `starter/app` 中的配置文件复制到相应位置（包括 `.dockerignore`）。将阶段 00 的任务总结模板复制为本任务的 `任务总结.md`。

目录结构：

```text
app/
├── compose.yaml
├── backend/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
└── frontend/
    ├── Dockerfile
    ├── default.conf.template
    ├── package.json
    └── src/
```

## 第一步：调整应用路径

1. 让后端从环境变量 `DATABASE_PATH` 读取 SQLite 文件位置；没有设置时仍可使用本地开发默认路径。例如导入 `os`，用 `Path(os.getenv("DATABASE_PATH", "registrations.db"))` 生成数据库路径。
2. 配置容器使用 `/data/registrations.db`，Compose 将 `/data` 挂载到命名卷 `app-data`。数据库文件保存在卷中，不放进 Git 仓库。
3. 把 React 请求 API 的网址改为以 `/api` 开头，例如 `/api/events`。
4. 在 Compose 中将 `API_ORIGIN` 设为 `http://api:8000`。查看 `default.conf.template`：前端容器负责提供打包后的网页，并把 `/api/` 请求转发给 API 容器。这样前端和 API 使用同一个入口，不需要对公网开放 API 端口。

## 第二步：本地手动启动

在 `app` 目录执行：

```powershell
docker compose up --build
```

访问 `http://localhost:8080`，测试查看活动、新增报名、修改和删除。打开另一个终端检查容器状态：

```powershell
docker compose ps
```

停止应用：

```powershell
docker compose down
```

再次运行并刷新页面，确认报名数据仍保存在命名卷中。不要使用 `docker compose down -v`，它会删除命名卷和其中的数据。

## 提交内容

提交 Dockerfile、`compose.yaml`、Nginx 配置、为容器运行所需的源码修改和 `任务总结.md`。不要提交 `.db`、`.env`、密钥、`node_modules` 或 Docker 镜像。

```powershell
git status
git add 04-1-Docker打包与本地运行
git commit -m "Run the activity app with Docker Compose"
git push origin main
```

## 完成检查

- [ ] Compose 能构建并启动前端和 API。
- [ ] React 页面能通过 `/api` 访问后端，完整 CRUD 可用。
- [ ] 重启容器后，报名记录仍然存在。
- [ ] API 容器端口没有映射到公网；未提交数据库、密钥或 `.env`。
