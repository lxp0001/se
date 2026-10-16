-- 任务 01-2：SQLite 参考答案（教师用）
-- 可在 SQLite 命令行或 DBX 的 SQL 编辑器中执行。
-- 所有用户名均为虚构代号。

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS registrations (
    id INTEGER PRIMARY KEY,
    event_id INTEGER NOT NULL REFERENCES events(id),
    student_name TEXT NOT NULL
);

-- 清除旧样例，保证重复执行后仍是同一组数据。
-- 先清报名表（子表），再清活动表（父表）。
DELETE FROM registrations;
DELETE FROM events;

INSERT INTO events (id, name) VALUES
    (1, '机器人体验'),
    (2, '校园摄影');

INSERT INTO registrations (id, event_id, student_name) VALUES
    (1, 1, 'user1'),
    (2, 1, 'user2'),
    (3, 2, 'user1');

-- 查看所有报名记录。
SELECT events.name AS event_name,
       registrations.student_name
FROM registrations
JOIN events ON registrations.event_id = events.id
ORDER BY registrations.id;

-- 查询 user1 报名的活动。
SELECT events.name AS event_name
FROM registrations
JOIN events ON registrations.event_id = events.id
WHERE registrations.student_name = 'user1'
ORDER BY events.id;

-- 查询不存在的 user3 有几条报名记录，预期为 0。
SELECT COUNT(*) AS registration_count
FROM registrations
WHERE student_name = 'user3';
