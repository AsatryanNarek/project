import sqlite3


DB_NAME = "blog.db"
conn = sqlite3.connect(DB_NAME)
conn.row_factory = sqlite3.Row

conn.executemany("""
            INSERT INTO sections (name, slug)
            VALUES (?, ?)""",
                 [("1", "my-hobbies"),
                  ("2", "ceramics"),
                  ("3", "anime")],
                 )
conn.commit()
conn.close()
