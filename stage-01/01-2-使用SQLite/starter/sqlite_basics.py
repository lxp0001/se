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
    cursor = connection.cursor()

    # TODO 1：创建 events 表。
    # 字段：id（整数主键）、name（必填文字）。

    # TODO 2：创建 registrations 表。
    # 字段：id（整数主键）、event_id（必填整数，关联 events.id）、
    # student_name（必填文字）。

    # TODO 3：为了可重复运行，先清空旧数据（先 registrations，再 events），
    #         然后把 events 和 registrations 中的数据分别插入对应的表。

    # TODO 4：查询并打印全部报名记录；结果中同时显示活动名和报名者。

    # TODO 5：用参数化查询筛选 student_name，打印这个人报名的活动名称。

print(f"SQLite 数据库文件已生成：{DB_FILE.name}")
