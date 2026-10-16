# 任务 02-2：制作读取活动数据的 API

上一个任务让服务器返回固定消息。本任务让 API 从 SQLite 读取活动数据：一个接口列出所有活动，另一个根据活动编号读取单场活动。

## 完成后你应该能够

- 用 FastAPI 路径参数选择一条资源。
- 从 SQLite 读取记录，并把结果作为 JSON 返回。
- 说明数据库记录如何变成 HTTP 响应。
- 通过 `GET` 请求读取活动列表或单项活动。
- 看懂 RESTful 风格网址中资源集合与单项资源的区别。

## 先想一想

如果要查看所有活动和查看某一场活动，网址需要有什么不同？先把预测写进 `任务总结.md`。

## 开始前

完成 02-1。在仓库根目录创建 `02-2-读取活动数据API` 文件夹，复制 `starter/main.py`、`starter/requirements.txt` 和阶段 00 的任务总结模板。此任务使用虚构活动，并在本地初始化 SQLite 数据；不要提交生成的数据库文件。

## 第一步：启动并查看所有活动

安装依赖并启动服务器：

```powershell
pip install -r requirements.txt
uvicorn main:app --reload
```

访问 `http://127.0.0.1:8000/events`，观察活动列表及 JSON 响应。样例包含两项活动。这个接口使用 `GET`，也就是向服务器读取活动信息。

这里 `/events` 表示活动集合；接下来使用 `/events/{event_id}` 表示集合中的某一项活动。这种让网址对应资源、让请求方法表达操作的组织方式，叫 RESTful 风格。

## 第二步：补全单项活动接口

打开 `main.py`，补全 `get_event` 函数：

1. 从路径参数 `event_id` 取得活动编号。
2. 在 SQLite 中查找对应活动。
3. 找到时返回该活动的 `id` 和 `name`。
4. 找不到时返回 HTTP 404。

先预测访问 `/events/1` 与 `/events/999` 分别会得到什么，再通过 `/docs` 实际请求核对。

## 第三步：记录请求证据

在 `任务总结.md` 中记录列表接口的状态码和内容，以及两个单项查询的状态码；用一句话判断自己的预测是否正确。

## 提交内容

```text
02-2-读取活动数据API/
├── main.py
├── requirements.txt
└── 任务总结.md
```

本地生成的 `activities.db` 不提交。提交代码和总结：

```powershell
git status
git add 02-2-读取活动数据API
git commit -m "Read activities through an API"
git push origin main
```

## 完成检查

- [ ] `GET /events` 返回 SQLite 中的活动列表。
- [ ] `GET /events/{event_id}` 能返回指定活动。
- [ ] 查询不存在的编号返回 404，而不是服务器崩溃。
- [ ] 数据库文件未提交；任务总结含请求证据并已推送到 `main`。

## 过关方式

教师指定一个活动编号，请你预测响应并解释 API 是怎样把数据库中的活动变成 JSON 的。
