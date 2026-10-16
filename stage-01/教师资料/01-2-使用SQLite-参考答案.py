"""任务 01-2：SQLite 教师参考答案。"""

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

connection = sqlite3.connect(DB_FILE)
try:
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

    # 先清空子表，再清空父表，确保程序可以重复运行。
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

    missing_name = "user3"
    cursor.execute(
        "SELECT COUNT(*) FROM registrations WHERE student_name = ?",
        (missing_name,),
    )
    missing_count = cursor.fetchone()[0]
    print(f"\n{missing_name} 的报名记录数：{missing_count}")

    connection.commit()
finally:
    connection.close()

print(f"\nSQLite 数据库文件已生成：{DB_FILE.name}")
