# config/database.py
import sqlite3

def get_db_connection():
    # This creates a connection to a local file named library.db
    conn = sqlite3.connect('library.db')
    conn.row_factory = sqlite3.Row  # Allows accessing columns by name
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            status TEXT DEFAULT 'Available'
        )
    ''')
    conn.commit()
    conn.close()
