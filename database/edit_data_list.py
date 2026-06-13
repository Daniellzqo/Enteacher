import sqlite3
from pathlib import Path

def get_connection():
    path = Path("data/database.db")
    conn = sqlite3.connect(path)

    return conn




def insert_word(word, lang, list_id):
    conn= get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id from tbwords WHERE word like ? and list=? and lang=?
    """, (word, list_id, lang))

    row = cursor.fetchone()

    if row is None:
        cursor.execute("""
            INSERT INTO tbwords (word, list, lang) VALUES (?, ?, ?)
        """, (word, list_id, lang)) 

        conn.commit()
        word_id = cursor.lastrowid 
    else:
        word_id = row[0]

    return word_id


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
    

def update_word(wordid, word, translations, listid):
    
    list = [x.strip() for x in translations.split(",")]

    conn = get_connection()
    cursor = conn.cursor()


    

    list_id = listid
    
    if int(wordid) > 0:
        cursor.execute("""
            DELETE FROM tbwords WHERE id=?
        """, (wordid,))
    
        conn.commit()

        cursor.execute("""
            DELETE FROM tbtranslate WHERE wordid=?
        """, (wordid,))
    
        conn.commit()

    en_id = insert_word(word, "en", list_id)
    print(f"en id {en_id}")

    for trans in list:
        pl_id = insert_word(trans, "pl", list_id)
        print(f"pl id {pl_id}")
        cursor.execute("""
            INSERT INTO tbtranslate (wordid, translid) VALUES (?, ?)
        """, (en_id, pl_id)) 

        conn.commit()
    return "OK"

def save_word(listid, word, translation):
    import sqlite3

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO words (listid, word, translation)
        VALUES (?, ?, ?)
    """, (listid, word, translation))

    conn.commit()
    conn.close()

