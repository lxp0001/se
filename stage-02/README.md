# 阶段 02：HTTP、REST API 与服务器

本阶段承接阶段 01 的 SQLite 与活动报名数据，让学生理解浏览器或其他客户端如何通过 HTTP 向服务器请求数据。使用 FastAPI 构建本地 REST API；前端页面、自动化测试和云部署分别留到后续阶段。

| 编号 | 任务 | 先想一想 | 学生做出的东西 | 提交内容 |
| --- | --- | --- | --- | --- |
| 02-1 | [启动第一个 Web 服务器](02-1-第一个Web服务器/README.md) | 浏览器打开一个网址时，电脑另一端的程序怎样把数据送回来？ | 可运行的 FastAPI 服务和 JSON 响应 | `main.py`、`requirements.txt`、`任务总结.md` |
| 02-2 | [读取活动数据的 API](02-2-读取活动数据API/README.md) | 如何用一个网址查看所有活动，再用另一个网址查看指定活动？ | 从 SQLite 读取活动的列表和详情接口 | `main.py`、`requirements.txt`、`任务总结.md` |
| 02-3 | [报名记录的增删改查](02-3-提交报名与处理错误/README.md) | 报名后发现用户名写错了，怎样修改或取消，而不是重新报名？ | 为报名记录实现新增、查看、修改和删除 API | `main.py`、`requirements.txt`、`任务总结.md` |

## GET 与 POST

- `GET` 用来向服务器读取信息，例如查看活动列表或某场活动；本阶段 02-1 和 02-2 都会用到。
- `POST` 用来新增数据，例如提交报名；本阶段 02-3 会用到。
- `PATCH` 用来修改数据，`DELETE` 用来删除数据；本阶段 02-3 会用它们管理报名记录。
- 本阶段的 API 用 RESTful 风格组织：网址表示要操作的资源，例如 `/events` 表示活动集合、`/events/1` 表示编号为 1 的活动；请求方法表示要做的事，例如 GET 读取、POST 新增、PATCH 修改、DELETE 删除。
- 这些是便于组织接口的一组约定，不是要求学生背诵的复杂规则。学生通过 `/docs` 实际发送请求，观察网址、请求方法、请求内容和响应。

## 增删改查（CRUD）

| 操作 | 常见 HTTP 方法 | 活动 API 示例 | 本阶段安排 |
| --- | --- | --- | --- |
| 查 Read | `GET` | `GET /events`、`GET /events/1`、`GET /events/1/registrations` | 02-1、02-2、02-3 实作 |
| 增 Create | `POST` | `POST /events/1/registrations` | 02-3 实作 |
| 改 Update | `PATCH` | `PATCH /events/1/registrations/1` | 02-3 实作 |
| 删 Delete | `DELETE` | `DELETE /events/1/registrations/1` | 02-3 实作 |

本阶段先通过活动 API 练习读取，再在报名记录上完成新增、查看、修改和删除，形成完整 CRUD。阶段 03 直接用 React 页面调用这些 API；只讲完成 React 任务所需的 JavaScript 基础，不单独设置 JavaScript 阶段。

## 阶段约定

- 每项任务先预测请求结果，再运行服务器并观察浏览器/API 文档中的响应，最后在任务总结里回顾预测是否正确。
- 使用虚构活动和 `user1`、`user2` 等用户名；不要提交真实个人资料或密钥。
- 数据库只在本地生成，沿用阶段 00 的 `.gitignore`，不提交 `.db` 文件。
- 本阶段只在本机运行服务，不做 JavaScript 前端、CORS 配置、自动化测试、Docker 或云部署。
- 每项任务放入个人仓库对应目录，按前序阶段方式提交到个人仓库 `main` 分支。

## 完成标准

能够说明客户端请求、服务器处理和 HTTP 响应之间的关系；能够用 FastAPI 提供 JSON 接口，从 SQLite 读取和写入数据，并对成功、缺失资源和无效输入返回合理结果。
