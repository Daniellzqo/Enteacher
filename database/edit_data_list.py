import sqlite3
from pathlib import Path

def get_connection():
    path = Path("data/database.db")
    conn = sqlite3.connect(path)

    return conn

def insert_list(listname, worden, wordpl):
    conn = get_connection()
    cursor = conn.cursor()

    #insert list
    cursor.execute("""
        SELECT id from tblist WHERE listname like ?  
    """, (listname,))

    row = cursor.fetchone()

    if row is None:
        cursor.execute("""
            INSERT INTO tblist (listname) VALUES (?)
        """, (listname,)) 

        conn.commit()
        list_id = cursor.lastrowid 
    else:
        list_id = row[0]


    #insert en word
    cursor.execute("""
        SELECT id from tbwords WHERE word like ? and list=? and lang='en'
    """, (worden, list_id))

    row = cursor.fetchone()

    if row is None:
        cursor.execute("""
            INSERT INTO tbwords (word, list, lang) VALUES (?, ?, ?)
        """, (worden, list_id, "en")) 

        conn.commit()
        worden_id = cursor.lastrowid 
    else:
        worden_id = row[0]


    #insert pl word
    cursor.execute("""
        SELECT id from tbwords WHERE word like ? and list=? and lang='pl'
    """, (wordpl, list_id))

    row = cursor.fetchone()

    if row is None:
        cursor.execute("""
            INSERT INTO tbwords (word, list, lang) VALUES (?, ?, ?)
        """, (wordpl, list_id, "pl")) 

        conn.commit()
        wordpl_id = cursor.lastrowid 
    else:
        wordpl_id = row[0]
        
    
    #transl
    cursor.execute("""
        SELECT id from tbtranslate WHERE wordid = ? and translid=? 
    """, (worden_id, wordpl_id))

    row = cursor.fetchone()

    if row is None:
        cursor.execute("""
            INSERT INTO tbtranslate (wordid, translid) VALUES (?, ?)
        """, (worden_id, wordpl_id)) 

        conn.commit()
        transl_id = cursor.lastrowid 
    else:
        transl_id = row[0]


    return transl_id
    



