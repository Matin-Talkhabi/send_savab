import sqlite3

DB_NAME = "users.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            time TEXT,
            mode TEXT,
            chapter INTEGER,
            verse INTEGER
        )
    """)
    conn.commit()
    conn.close()

def get_user(user_id):
    try:
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            result = c.fetchone()
        return result
    except sqlite3.Error as e:
        logger.error(f"خطا در دریافت اطلاعات کاربر {user_id}: {e}")
        return None



def set_user_time(user_id, time_str):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        INSERT INTO users (id, time) VALUES (?, ?)
        ON CONFLICT(id) DO UPDATE SET time=excluded.time
    """, (user_id, time_str))
    conn.commit()
    conn.close()

def set_user_mode(user_id, mode):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        INSERT INTO users (id, mode) VALUES (?, ?)
        ON CONFLICT(id) DO UPDATE SET mode=excluded.mode
    """, (user_id, mode))
    conn.commit()
    conn.close()

def update_user_position(user_id, chapter, verse):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        INSERT INTO users (id, chapter, verse) VALUES (?, ?, ?)
        ON CONFLICT(id) DO UPDATE SET chapter=excluded.chapter, verse=excluded.verse
    """, (user_id, chapter, verse))
    conn.commit()
    conn.close()

def add_user_if_not_exists(user_id):
    if not get_user(user_id):
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("INSERT INTO users (id) VALUES (?)", (user_id,))
        conn.commit()
        conn.close()

def update_user(user_id, **kwargs):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    fields = ', '.join(f"{k}=?" for k in kwargs)
    values = list(kwargs.values()) + [user_id]
    c.execute(f"UPDATE users SET {fields} WHERE id = ?", values)
    conn.commit()
    conn.close()
