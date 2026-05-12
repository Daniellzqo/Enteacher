import sqlite3
from pathlib import Path

def get_connection():
    path = Path("data/database.db")
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn

def get_lists():
    conn = get_connection()

    result = conn.execute("SELECT * FROM tblist")
    lists = result.fetchall()
    print(lists)
    return lists   



