import sqlite3

def get_db():
    conn = sqlite3.connect("backend/db/ai_news.db")
    return conn

def init_db():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY,
            source TEXT,
            title TEXT,
            link TEXT,
            summary TEXT
        )
    ''')
    db.commit()