import sqlite3
from pathlib import Path

def get_connection():
    path = Path("data/database.db")
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn

def get_words(id):
    conn = get_connection()
    result = conn.execute("SELECT * FROM tbwords WHERE list = ?", (id,)) 

    words = result.fetchall()
    return words  




