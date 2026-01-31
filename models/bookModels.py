# models/bookModel.py (Now acting as a Repository)
from config.database import get_db_connection

class BookRepository:
    def __init__(self):
        self.db = get_db_connection()

    def get_all(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM books")
        return [dict(row) for row in cursor.fetchall()]
