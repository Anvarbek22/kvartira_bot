import psycopg2 

def create_read():
    try:
        connection=psycopg2.connect(user='postgres',password='193758462',database='kvartira_db',host='localhost',port=5432)
        print('connect')
        cur=connection.cursor()
        cur.execute('SELECT * FROM SINGIN')
        data=cur.fetchall()
        return data
    except:
        print('Error')


def create_add(ID,USER_NAME,PHONE_NUM,MALE,DATE):
    try:
        connection=psycopg2.connect(user='postgres',password='193758462',database='kvartira_db',host='localhost',port=5432)
        print('connect')
        cur=connection.cursor()
        table='''INSERT INTO SINGIN(ID,USER_NAME,PHONE_NUM,MALE,DATE) VALUES (%s,%s,%s,%s,%s)'''
        cur.execute(table,(ID,USER_NAME,PHONE_NUM,MALE,DATE))
        connection.commit()
    except:
        print('Error')


def create_del(ids):
    try:
        connection=psycopg2.connect(user='postgres',password='193758462',database='kvartira_db',host='localhost',port=5432)
        print('connect')
        cur=connection.cursor()
        table='''DELETE FROM SINGIN 
                 WHERE ID= %s'''
        cur.execute(table,(ids))
        connection.commit()
    except:
        print('Error')


def create_table():
    try:
        connection=psycopg2.connect(user='postgres',password='193758462',database='kvartira_db',host='localhost',port=5432)
        print('connect')
        cur=connection.cursor()
        table='''CREATE TABLE MAKEFRIEND(ID TEXT NOT NULL,
                                    USER_NAME TEXT NOT NULL,
                                    PHONE_NUM TEXT NOT NULL,
                                    MALE TEXT NOT NULL,
                                    DATE TEXT NOT NULL,
                                    UNIVERSITET TEXT,
                                    YONALISH TEXT)'''
        cur.execute(table)
        connection.commit()
    except:
        print('Error')
          
def make_friend_db(ids):
    data=create_read()
    for i in data:
        if str(ids)==i[0]:
            ID=i[0]
            USER_NAME=i[1]
            PHONE_NUM=i[2]
            MALE=i[3]
            DATE=i[4]
            UNIVERSITET=' '
            YONALISH=' '
    
    try:
        connection=psycopg2.connect(user='postgres',password='193758462',database='kvartira_db',host='localhost',port=5432)
        print('connect')
        cur=connection.cursor()
        table='''INSERT INTO MAKEFRIEND(ID,USER_NAME,PHONE_NUM,MALE,DATE,UNIVERSITET,YONALISH) VALUES (%s,%s,%s,%s,%s,%s,%s)'''
        cur.execute(table,(ID,USER_NAME,PHONE_NUM,MALE,DATE,UNIVERSITET,YONALISH))
        connection.commit()
    except:
        print('Error')