import sqlite3
from pathlib import Path

def get_connection():
    path = Path("data/database.db")
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn

def get_words(id, lang):
    conn = get_connection()
    result = conn.execute("""
        SELECT 
            w.id,
            w.word,
            w.list,

            GROUP_CONCAT(tw.word, ', ') AS translations
        FROM tbwords w

        LEFT JOIN tbtranslate tr
            ON tr.wordid = w.id

        LEFT JOIN tbwords tw
            ON tw.id = tr.translid

        WHERE w.list = ?
          AND w.lang = ?

        GROUP BY w.id, w.word, w.list
    """, (id, lang))

    words = result.fetchall()
    return words  


def get_word_transl(listid):
    conn = get_connection()

    result = conn.execute("""
        SELECT 
            w.id,
            w.word,
            IFNULL(GROUP_CONCAT(tw.word, ', '), '') AS translation
        FROM tbwords w

        LEFT JOIN tbtranslate tr
            ON tr.wordid = w.id

        LEFT JOIN tbwords tw
            ON tw.id = tr.translid

        WHERE w.list = ?

        GROUP BY w.id, w.word
    """, (listid,))

    return [dict(r) for r in result.fetchall()]



