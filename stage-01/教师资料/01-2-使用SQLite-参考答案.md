# 任务 01-2：使用 SQLite 参考答案（教师用）

本页供教师备课和核对使用，不作为学生 starter。学生答案可以有不同写法，只要表结构、数据和查询结果正确，并能解释即可。

另附[完整 Python 答案代码](01-2-使用SQLite-参考答案.py)和[完整 SQL 答案文件](01-2-使用SQLite-参考答案.sql)。SQL 文件可在 SQLite 命令行或 DBX 的 SQL 编辑器中执行；Python 程序展示如何从代码中完成相同操作。两者是两种独立的参考做法。

## 完整参考程序

```python
"""SQLite 基础：建表、插入虚构数据并查询。"""

import sqlite3
from pathlib import Path


DB_FILE = Path(__file__).with_name("registrations.db")
student_name = "user1"

events = [
    (1, "机器人体验"),
    (2, "校园摄影"),
]
registrations = [
    (1, 1, "user1"),
    (2, 1, "user2"),
    (3, 2, "user1"),
]

with sqlite3.connect(DB_FILE) as connection:
    # SQLite 默认不强制检查外键；本任务显式开启，便于理解表之间的关联。
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY,
            event_id INTEGER NOT NULL REFERENCES events(id),
            student_name TEXT NOT NULL
        )
    """)

    # 先清空子表，再清空父表；保证程序可以重复运行。
    cursor.execute("DELETE FROM registrations")
    cursor.execute("DELETE FROM events")

    cursor.executemany(
        "INSERT INTO events (id, name) VALUES (?, ?)",
        events,
    )
    cursor.executemany(
        "INSERT INTO registrations (id, event_id, student_name) VALUES (?, ?, ?)",
        registrations,
    )

    print("全部报名记录：")
    cursor.execute("""
        SELECT events.name, registrations.student_name
        FROM registrations
        JOIN events ON registrations.event_id = events.id
        ORDER BY registrations.id
    """)
    for event_name, attendee in cursor.fetchall():
        print(f"{event_name}：{attendee}")

    print(f"\n{student_name} 报名的活动：")
    cursor.execute("""
        SELECT events.name
        FROM registrations
        JOIN events ON registrations.event_id = events.id
        WHERE registrations.student_name = ?
        ORDER BY events.id
    """, (student_name,))
    for (event_name,) in cursor.fetchall():
        print(event_name)

    # 验证不存在的用户名能正常查出空结果。
    missing_name = "user3"
    cursor.execute(
        "SELECT COUNT(*) FROM registrations WHERE student_name = ?",
        (missing_name,),
    )
    missing_count = cursor.fetchone()[0]
    print(f"\n{missing_name} 的报名记录数：{missing_count}")

connection.close()
print(f"\nSQLite 数据库文件已生成：{DB_FILE.name}")
```

## 预期结果

```text
全部报名记录：
机器人体验：user1
机器人体验：user2
校园摄影：user1

user1 报名的活动：
机器人体验
校园摄影

user3 的报名记录数：0

SQLite 数据库文件已生成：registrations.db
```

## 讲解要点

- `sqlite3.connect(DB_FILE)`：连接数据库；文件不存在时自动创建数据库文件。
- `CREATE TABLE IF NOT EXISTS`：在数据库中创建表；重复运行不会因表已存在而失败。
- `INTEGER PRIMARY KEY`：为每行记录提供唯一编号。
- `REFERENCES events(id)`：表示报名记录中的活动编号关联到活动表。
- `DELETE` 后重新插入固定样例：让程序重复运行时仍得到相同数据；先删报名记录，再删活动记录。
- `executemany`：将多行数据批量插入；`?` 是参数占位符，数据与 SQL 结构分开传递。
- `JOIN`：根据活动编号把活动名称和报名者信息组合起来。
- `fetchall()` / `fetchone()`：分别取回多条查询结果和一条汇总结果。
- `with sqlite3.connect(...) as connection`：正常结束时自动提交事务；异常时回滚。它不会自动关闭连接，因此代码块结束后显式调用 `connection.close()`。

`.db` 是程序生成的本地数据库，不应提交到学生仓库；课程 `.gitignore` 已包含对应规则。用户名均为虚构代号。
