# service/bookService.py
class Book:
    def __init__(self, title): self.title = title

class LibraryItemFactory:
    @staticmethod
    def create_item(item_type, title):
        if item_type == "book":
            return Book(title)
        # Easy to scale to 'magazine' or 'dvd' later
        return None
