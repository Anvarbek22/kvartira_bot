import sqlite3

def create_del(PHONE):
    conn = sqlite3.connect('DB/SERVER/CAI_HISOB_SQL.DB')
    cur = conn.cursor()
    TABLE='''DELETE FROM TELEGRAM_BOT WHERE ID=?'''
    cur.execute(TABLE,(PHONE,))
    conn.commit()
    create_kvartira_del(PHONE)

def create_kvartira_del(PHONE):
    conn = sqlite3.connect('DB/SERVER/CAI_KVARTIRA_SQL.DB')
    cur = conn.cursor()
    TABLE='''DELETE FROM TELEGRAM_BOT WHERE ID=?'''
    cur.execute(TABLE,(PHONE,))
    conn.commit()

def create_del2(PHONE):
    conn = sqlite3.connect('DB/SERVER/CAI_HISOB_SQL.DB')
    cur = conn.cursor()
    TABLE='''DELETE FROM TELEGRAM_BOT WHERE PHONE_NUM=?'''
    cur.execute(TABLE,(PHONE,))
    conn.commit()
    create_kvartira_del2(PHONE)

def create_kvartira_del2(PHONE):
    conn = sqlite3.connect('DB/SERVER/CAI_KVARTIRA_SQL.DB')
    cur = conn.cursor()
    TABLE='''DELETE FROM TELEGRAM_BOT WHERE PHONE_NUM=?'''
    cur.execute(TABLE,(PHONE,))
    conn.commit()