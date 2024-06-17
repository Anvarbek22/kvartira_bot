import psycopg2

def create_read():
    try:
        connection=psycopg2.connect(user='postgres',password='193758462',database='kvartira_db',host='localhost',port=5432)
        print('connect')
        cur=connection.cursor()
        table='''SELECT * FROM SINGIN;'''
        cur.execute(table)
        data=cur.fetchall()
        connection.commit()
        return data
    except:
        print('Error')