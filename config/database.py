# config/database.py
import sqlite3

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = sqlite3.connect('library.db', check_same_thread=False)
            cls._instance.row_factory = sqlite3.Row
        return cls._instance

def get_db_connection():
    return DatabaseConnection()
