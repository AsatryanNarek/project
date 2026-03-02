import sqlite3


DB_NAME = "blog.db"
conn = sqlite3.connect(DB_NAME)
conn.row_factory = sqlite3.Row


conn.executemany("""
            INSERT INTO sections (name, slug)
            VALUES (?, ?)""",
                 [("Біографії", "biohrafii"),
                  ("Географія", "heohrafiia"),
                  ("Природа", "pryroda"),
                  ("Спорт", "sport"),
                  ("Технології", "tekhnolohii"),
                  ("Україна", "ukraina"),
                  ("Філософія", "filosofiia"),
                  ("Наука", "nauka"),
                  ],
                 )
conn.commit()
conn.close()


