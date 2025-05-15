import sqlite3

# 连接到本地数据库文件（如果文件不存在会自动创建）
conn = sqlite3.connect("example.db")

# 创建游标对象
cursor = conn.cursor()

# 创建表
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
""")
conn.commit()

# 插入数据
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Tom", 23))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Yarn", 20))
conn.commit()

# 查询数据
cursor.execute("SELECT * FROM users")
print(cursor.fetchone())
print()
# (1, 'Alice', 25)

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)
print()
# (1, 'Alice', 25)
# (2, 'Tom', 23)
# (3, 'Yarn', 20)

cursor.execute("SELECT * FROM users")
rows = cursor.fetchmany(2)
for row in rows:
    print(row)
print()
# (1, 'Alice', 25)
# (2, 'Tom', 23)

# 更新和删除
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (26, "Alice"))
cursor.execute("DELETE FROM users WHERE name = ?", ("Tom",))
conn.commit()

# 查询数据
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)
# (1, 'Alice', 26)
# (3, 'Yarn', 20)

# 关闭游标和连接
cursor.close()
conn.close()
