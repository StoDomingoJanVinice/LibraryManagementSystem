# services/bookService.py
class BookService:
    def __init__(self, model):
        self.model = model

    def get_available_books(self):
        """Contains logic to only return books that are not borrowed"""
        all_books = self.model.get_all_books()
        # Logic: Filter books where status is 'Available'
        available = [b for b in all_books if b['status'] == 'Available']
        return available
