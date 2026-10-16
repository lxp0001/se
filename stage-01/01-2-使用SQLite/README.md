# 任务 01-2：用 SQLite 保存和查询报名记录

JSON 适合直观地保存一小份数据。本任务开始使用 SQLite：它会把数据放进本地数据库文件，并提供 SQL 语句来筛选记录。我们仍使用虚构的活动报名名单。

## 完成后你应该能够

- 解释数据库、表、记录和字段的基本含义。
- 使用 Python 的 `sqlite3` 创建表、插入记录并查询。
- 用参数化查询按报名者查找活动。

## 先想一想

想查“user1 报了哪些活动”，在 JSON 里要怎么做？你猜数据库能一句话做到吗？先把预测写进 `任务总结.md`。

## 开始前

完成 01-1，并将任务成果推送到个人仓库 `main`。同步仓库后，在根目录创建 `01-2-使用SQLite` 文件夹，复制 `starter/sqlite_basics.py` 和阶段 00 的任务总结模板。

SQLite 数据库会在本地生成。阶段 00 提供的 `.gitignore` 已忽略生成的 `.db`、`.sqlite` 和 `.sqlite3` 文件；不要把它们提交到 GitHub，提交 Python 源码和查询结果文字即可。若你沿用的旧版 `.gitignore` 尚无这些规则，请补上：

```gitignore
*.db
*.sqlite
*.sqlite3
```

本任务继续只用虚构数据，不放真实个人信息、密码或密钥。

## 第一步：看懂表格

本任务把数据拆成两张表：

| 表名 | 字段 | 类型与要求 |
| --- | --- | --- |
| `events` | `id` | 整数；主键，每场活动的唯一编号 |
| `events` | `name` | 文字；必填，活动名称 |
| `registrations` | `id` | 整数；主键，每条报名记录的唯一编号 |
| `registrations` | `event_id` | 整数；必填，关联 `events.id` |
| `registrations` | `student_name` | 文字；必填，虚构用户名 |

例如 user1 报了两场活动，在 `registrations` 表中会有两行。活动编号把报名记录和活动信息连起来。请根据上表自行编写建表语句；本任务书不提供 SQL 语句。

## 第二步：完成程序

打开 `sqlite_basics.py`，按 TODO 完成以下步骤：

1. 用 `sqlite3.connect` 连接 `registrations.db`。如果文件还不存在，SQLite 会自动创建数据库文件；这一步还没有创建表。
2. 在连接内用 `cursor.execute()` 执行你自己编写的建表语句，按上表创建 `events` 和 `registrations` 两张表。整数类型用于编号，文字类型用于活动名和用户名；将各表的 `id` 设为主键，并让 `registrations.event_id` 关联 `events.id`。先创建 `events`，再创建 `registrations`。

3. 每次运行先清空旧数据（先删 `registrations`，再删 `events`），随后插入两场活动和至少三条虚构报名记录；这样重复运行也不会因编号重复出错。
4. 查询所有报名记录并打印。
5. 查询 user1 报名的活动，并打印活动名称。

运行 starter：

```powershell
py 01-2-使用SQLite/sqlite_basics.py
```

查询时使用参数化查询，将用户名作为参数传入，不要把变量值直接拼接进 SQL 字符串。这是更安全、可靠的习惯。

**选做：**程序运行并生成 `registrations.db` 后，可以用 [DBX](https://dbxio.com/en) 打开数据库，查看 `events`、`registrations` 两张表及其中的记录。DBX 只是可选的图形化查看工具，不要求安装，也不能替代本任务中的 Python/SQL 编程。

## 第三步：预测并核对查询

运行前先预测：user1 会查到几场活动？查询结果中的活动名称是什么？运行后把实际结果写入 `任务总结.md`，并用一句话判断预测是否正确。

再把查询用户名改成名单里没有的 `user3`，观察结果。恢复为 user1 后保存最终代码。

## 提交清单

```text
个人仓库/
└── 01-2-使用SQLite/
    ├── sqlite_basics.py
    └── 任务总结.md
```

`registrations.db` 由程序在本地生成，不放入提交目录，也不要提交。提交前运行 `git status`，确认数据库文件未被追踪；然后按阶段 00 的方式提交并推送到 `main`。

```powershell
git status
git add 01-2-使用SQLite
git commit -m "Create and query a SQLite database"
git push origin main
```

## 完成检查

- [ ] 程序可重复运行，并建立表、插入和查询记录。
- [ ] 查询 user1 和不存在用户名的结果都符合预期。
- [ ] 查询使用 `?` 参数占位符，没有把用户输入拼到 SQL 中。
- [ ] 没有提交数据库文件、真实个人信息或密钥。
- [ ] 总结记录预测、实际结果及是否正确；任务已推送到个人仓库 `main`。

## 过关方式

教师随机指定一个姓名，请你预测查询结果并现场运行；再请你指出哪一段 SQL 负责筛选，以及活动编号怎样关联两张表。
