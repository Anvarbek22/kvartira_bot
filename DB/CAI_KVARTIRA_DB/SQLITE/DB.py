import sqlite3

def create_read():
    conn = sqlite3.connect('DB/SERVER/CAI_KVARTIRA_SQL.DB')
    cur = conn.cursor()
    TABLE='''SELECT * FROM TELEGRAM_BOT'''
    cur.execute(TABLE)
    data=cur.fetchall()
    return data

def create_update(ID,UNIVERSITET,YONALISH,URL):
    conn = sqlite3.connect('DB/SERVER/CAI_KVARTIRA_SQL.DB')
    cur = conn.cursor()
    TABLE='''UPDATE TELEGRAM_BOT SET UNIVERSITET=? WHERE ID=?'''
    cur.execute(TABLE,(UNIVERSITET,ID))
    TABLE='''UPDATE TELEGRAM_BOT SET YONALISH=? WHERE ID=?'''
    cur.execute(TABLE,(YONALISH,ID))
    TABLE='''UPDATE TELEGRAM_BOT SET URL=? WHERE ID=?'''
    cur.execute(TABLE,(URL,ID))
    conn.commit()

def create_deld():
    conn = sqlite3.connect('DB/SERVER/CAI_KVARTIRA_SQL.DB')
    cur = conn.cursor()
    TABLE='''DELETE FROM TELEGRAM_BOT'''
    cur.execute(TABLE)
    conn.commit()
