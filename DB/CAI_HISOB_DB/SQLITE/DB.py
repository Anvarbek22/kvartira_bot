import sqlite3

def create_add(ID,CMAIL,PASSWORD):
    conn = sqlite3.connect('DB/SERVER/CAI_HISOB_SQL.DB')
    cur = conn.cursor()
    TABLE='''INSERT INTO TELEGRAM_BOT(ID,CMAIL,PASSWORD) VALUES (?, ?, ?)'''
    cur.execute(TABLE,(ID,CMAIL,PASSWORD))
    conn.commit()


def create_add3(ID):
    TF="True"
    conn = sqlite3.connect('DB/SERVER/ECHO_SQL.DB')
    cur = conn.cursor()
    TABLE='''INSERT INTO TELEGRAM_BOT(ID,TF) VALUES (?,?)'''
    cur.execute(TABLE,(ID,TF))
    conn.commit()


def create_read3():
    conn = sqlite3.connect('DB/SERVER/ECHO_SQL.DB')
    cur = conn.cursor()
    TABLE='''SELECT * FROM TELEGRAM_BOT;'''
    cur.execute(TABLE)
    data=cur.fetchall()
    return data


def create_del3(ids):
    conn = sqlite3.connect('DB/SERVER/ECHO_SQL.DB')
    cur = conn.cursor()
    TABLE='''DELETE FROM TELEGRAM_BOT WHERE ID=?'''
    cur.execute(TABLE,(ids,))
    conn.commit()


def create_read():
    conn = sqlite3.connect('DB/SERVER/CAI_HISOB_SQL.DB')
    cur = conn.cursor()
    TABLE='''SELECT * FROM TELEGRAM_BOT;'''
    cur.execute(TABLE)
    data=cur.fetchall()
    return data

def create_add2(ID):
    data=create_read()
    for i in data:
        if i[0]==str(ID):
            ID=i[0]
            USER_NAME=i[1]
            PHONE_NUM=i[2]
            MALE=i[3]
            DATE=i[4]
            UNIVERSITET=" "
            YONALISH=" "
    
    conn = sqlite3.connect('DB/SERVER/CAI_KVARTIRA_SQL.DB')
    cur = conn.cursor()
    TABLE='''INSERT INTO TELEGRAM_BOT(ID,USER_NAME,PHONE_NUM,MALE,DATE,UNIVERSITET,YONALISH) VALUES (?, ?, ?, ?, ?, ?, ?)'''
    cur.execute(TABLE,(ID,USER_NAME,PHONE_NUM,MALE,DATE,UNIVERSITET,YONALISH))
    conn.commit()
    
    
    
def create():
    conn = sqlite3.connect('DB/SERVER/CAI_HISOB_SQL.DB')
    cur = conn.cursor()
    TABLE='''CREATE TABLE TELEGRAM_BOT(ID TEXT NOT NULL, CMAIL TEXT NOT NULL, PASSWORD TEXT NOT NULL)'''
    cur.execute(TABLE)
    conn.commit()

