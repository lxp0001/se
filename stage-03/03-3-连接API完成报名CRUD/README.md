# 任务 03-3：连接 API，完成报名 CRUD

上一任务的活动数据只保存在浏览器内存中，刷新页面就会回到初始值。本任务让 React 页面连接阶段 02 的 FastAPI 服务，让报名记录从 SQLite 读取并保存。

## 完成后你应该能够

- 在 React 页面加载时向 FastAPI 发出 GET 请求。
- 通过 POST、PATCH、DELETE 操作报名记录。
- 根据服务器响应显示更新后的列表和错误提示。

## 开始前

完成阶段 02 的 02-3 和阶段 03 的 03-2。使用阶段 02 已实现的报名 API，确保服务在 `http://127.0.0.1:8000` 正常运行；React 开发服务器也需要保持运行。

本任务中浏览器页面与 API 使用不同端口，浏览器可能因同源安全限制拦截请求。先在 FastAPI 中只允许本地 React 开发网址访问：在 `app = FastAPI(...)` 后配置 `CORSMiddleware`，把允许来源限定为 `http://localhost:5173` 和 `http://127.0.0.1:5173`。参考 [FastAPI 官方 CORS 文档](https://fastapi.tiangolo.com/tutorial/cors/)；不要为了省事设置任意来源。若 Vite 使用了其他端口，要把实际网址加入允许来源。

## 第一步：从服务器读取活动和报名

使用 React 的 `useEffect` 在页面加载时请求：

- `GET http://127.0.0.1:8000/events`：活动列表。
- 对每项活动请求 `GET http://127.0.0.1:8000/events/{event_id}/registrations`：报名列表。

把服务器返回的数据保存到 React 状态并显示。页面加载时显示“正在加载…”，请求失败时显示可读的错误信息。

## 第二步：提交新报名

在活动旁加入用户名输入框和报名按钮。提交时发送：

- 方法：`POST`
- 地址：`http://127.0.0.1:8000/events/{event_id}/registrations`
- JSON 请求体：`{"username":"user1"}`

成功后重新读取该活动的报名列表，或用响应数据更新页面。测试不存在的活动和空用户名，向学生展示服务器的错误响应；只使用 `user1`、`user2` 等虚构用户名。

## 第三步：修改和删除报名

在报名列表中为每条记录提供修改和删除操作：

- 修改：`PATCH /events/{event_id}/registrations/{registration_id}`，JSON 请求体例如 `{"username":"user2"}`。
- 删除：`DELETE /events/{event_id}/registrations/{registration_id}`。

请求成功后更新页面，并在浏览器刷新后确认数据仍与服务器一致。失败时显示错误，不要让界面假装操作成功。

## 提交内容

提交 React 项目源码、锁文件、必要的 FastAPI CORS 配置修改和 `任务总结.md`。不得提交数据库文件、`node_modules`、`.env` 或密钥。

```powershell
git status
git add 03-3-连接API完成报名CRUD
git commit -m "Connect React to the registration API"
git push origin main
```

## 完成检查

- [ ] React 页面显示服务器中的活动和报名数据。
- [ ] 新增、修改、删除后，页面与服务器数据一致。
- [ ] 刷新页面后仍能看到服务器保存的结果。
- [ ] 加载失败或请求被拒绝时，页面显示错误提示。
- [ ] CORS 只允许本地开发来源；没有提交数据库、`node_modules`、`.env`、密钥或真实个人信息。
