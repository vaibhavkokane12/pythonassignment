import sqlite3
def get_connection():
    with sqlite3.connect('todoapp.db') as conn:
        return conn