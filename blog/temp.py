import sqlite3


DB_NAME = "blog.db"
conn = sqlite3.connect(DB_NAME)
conn.row_factory = sqlite3.Row

conn.executemany("""
            INSERT INTO sections (name, slug)
            VALUES (?, ?)""",
                 [("Пожертвувати", "Sacrifice"),
                  ("Створити обліковий запис", "Create_an_account"),
                  ("Увійти", "Sign_in")],
                 )
conn.commit()
conn.close()
