# models/bookModel.py
from config.database import get_db_connection

class BookModel:
    def get_all_books(self):
        """Connects to the database and fetches all book records"""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Simple query to get data
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        
        # Convert sqlite rows to a list of dictionaries
        books = [dict(row) for row in rows]
        
        conn.close()
        return books
