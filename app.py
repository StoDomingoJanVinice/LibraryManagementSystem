# app.py
from config.database import init_db
from models.bookModel import BookModel
from services.bookService import BookService
from controllers.bookController import BookController

def bootstrap():
    """
    This function handles the 'Wiring' of the application.
    It follows the Dependency Injection pattern.
    """
    # 1. Initialize the Database (Create tables if they don't exist)
    print("[System] Initializing Database...")
    init_db()

    # 2. Instantiate the Model (Data Layer)
    model = BookModel()

    # 3. Instantiate the Service and Inject the Model
    # This keeps business logic separate from raw data access
    service = BookService(model)

    # 4. Instantiate the Controller and Inject the Service
    # The Controller doesn't know HOW the service works, just that it exists
    controller = BookController(service)

    return controller

def main():
    # Setup the MVC components
    library_controller = bootstrap()

    print("\n--- Welcome to the Library Management System ---")
    print("Architecture: Monolithic MVC")
    print("Pattern: Dependency Injection\n")

    # Trigger the controller logic to display books
    # In a real app, this would be triggered by a URL route or UI button
    library_controller.display_books()

if __name__ == "__main__":
    main()
