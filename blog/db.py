import sqlite3

DB_Name = "blog.db"

def get_db():
    conn = sqlite3.connect(DB_Name)
    conn.row_factory = sqlite3.Row
    return conn



def init_db():
    with get_db()as db:
        db.execute("""CREATE TABLE IF NOT EXISTS sections (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        slug TEXT UNIQUE NOT NULL
        )""")

        db.execute("""
        CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT NOT NULL, 
        image TEXT, 
        section_id INTEGER,
        created_at DATETTIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (section_id) REFERENCES sections(id)
        )
        """)


def get_blog_sections():
    with get_db() as db:
        sections = db.execute("SELECT * FROM sections")
        return sections


def get_section_by_slug(section_slug):
    with get_db() as db:
        sections = db.execute("SELECT * FROM sections WHERE slug = ?", (section_slug,)).fetchone()
        return sections


def get_section_by_id(section_id):
    with get_db() as db:
        sections = db.execute("SELECT * FROM sections WHERE id = ?", (section_id,)).fetchone()
        return sections


def get_section_posts(section_id):
    with get_db() as db:
        posts = db.execute("""
        SELECT * FROM posts 
        WHERE section_id = ?
        ORDER BY createt_at DESC 
        """, (section_id)).fetchall()

    return posts


def create_new_post(text, image, section_id):
    with get_db() as db:
        db.execute("""
                    INSERT INTO posts (text, image, section_id)
                    VALUES (?, ?, ?)
                """, (text, image, section_id))
        db.commit()

def sections():
    pass



if __name__ == "__main__":
    init_db()
