import sqlite3

connection = sqlite3.connect(-------------------)
connection.row_factory = sqlite3.Row

def get_database_connection():
    return connection