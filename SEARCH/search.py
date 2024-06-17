from DB.CAI_KVARTIRA_DB.SQLITE.DB import *

def db_search_user_uni(ID):
    data=create_read()
    mas=[]
    for i in data:
        if i[0]==str(ID):
            uni_search=i[5]
    for j in data:
        if j[5]==uni_search:
            mas.append([j[0],j[1]])
    return mas    

def db_search_user_yon(ID):
    data=create_read()
    mas=[]
    for i in data:
        if i[0]==str(ID):
            uni_search=i[6]
    for j in data:
        if j[6]==uni_search:
            mas.append([j[0],j[1]])
    return mas


def search_user(ID):
    a=[]
    data=create_read()
    for i in data:
        if i[0]==str(ID):
            a.append([i[7],f"Ism Familyasi: {i[1]}\nTalafon raqami: {i[2]}\nJinsi: {i[3]}\nTugilgan sanasi: {i[4]}\nO'qitotgan universiteti: {i[5]}\nO'qiyotgan yo'nalishi: {i[6]}"])    
    return a
    
    

def db_search(ids):
    data=create_read()
    for i in data:
        if i[0]==str(ids):
            return True
    else:
        return False
    
def db_search_test(ids):
    data=create_read()
    for i in data:
        if i[0]==str(ids):
            if i[5]==' ':
                return 'False'
            else:
                return 'True'
    else:
        return "Qayta urinib ko'ring"