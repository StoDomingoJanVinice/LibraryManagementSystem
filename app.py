# app.py
from config.database import init_db, get_db_connection
from models.bookModel import BookModel
from services.bookService import BookService
from controllers.bookController import BookController

def seed_data():
    """Adds sample data if the database is empty"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM books")
    if cursor.fetchone()[0] == 0:
        books = [
            ('The Great Gatsby', 'F. Scott Fitzgerald', 'Available'),
            ('1984', 'George Orwell', 'Available'),
            ('The Hobbit', 'J.R.R. Tolkien', 'Borrowed')
        ]
        cursor.executemany("INSERT INTO books (title, author, status) VALUES (?, ?, ?)", books)
        conn.commit()
    conn.close()

def main():
    # 1. Setup Database
    init_db()
    seed_data()

    # 2. Dependency Injection Integration
    model = BookModel()                  # Data Layer
    service = BookService(model)         # Business Layer (inject model)
    controller = BookController(service) # Application Layer (inject service)

    # 3. Execution
    print("System: Library Management System Started (Monolithic MVC)")
    controller.display_books()

if __name__ == "__main__":
    main()
