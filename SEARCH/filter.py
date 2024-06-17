from datetime import*
from DB.CAI_HISOB_DB.SQLITE.DB import *
def username(data):
    if len(data.split())==2:
        return True
    else:False

def cmail_filter(data):
    if str(data).endswith("@cmail.uz"):
        return True
    else:
        return "cmailingizni hato kiritdingiz"


def userid(ids):
    a=0
    data=create_read3()
    for i in data:
        if i[0]==str(ids):
            a=1
    if a==1:
        return True
    else:
        return False    


def db_search_del():
    mas=''
    data=create_read()
    for i in data:
        mas+=f"{i[2]}\n"
    return mas

def test_user(ids):
    a=0
    data=create_read()
    for i in data:
        if i[0]==str(ids):
            a=1
    if a==1:
        return True
    else:
        return False    

def datetest(data):
    def register(data):
        tests=0
        for i in str(data):
            if i.isdigit() or i.isalpha():
                pass
            else:
                if i!='/':
                    return False
                else:
                    data2=str(data).replace(i,' ')
        try:
            a,b,c=map(float,str(data2).split())
        except ValueError:
            return False
        if b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12:
            test1=31
        elif b==4 or b==6 or b==9 or b==11:
            test1=30
        elif b==2:
            test1=28
        else:
            test1=0
        
        if a<=test1:
            tests+=1
        if b<=12:
            tests+=1
        tests+=1
        if tests==3:
            return True
        else:
            return False
    if register(data):
        j=data.replace('/',' ')
        f=0
        now=datetime.now()
        b,n,m=map(int,str(j).split())
        fff1=datetime(m,n,b)
        nat2=now-fff1
        nat=nat2.days
        while nat>=365:
            if nat==0:
                break
            nat=nat-365
            f+=1
        k=0
        for i in range(m,now.year+1):
            if i%4==0:
                k+=1
        nat-=k
        l=0
        if f>=18:
            l+=1
        if nat>0:
            l+=1
        if l==2:
            return True
        else:
            return "Sizning yoshingiz kichik ekan\nsiz bu botdan foydalana olmaysiz"

    else:
        return "Siz tugulgan sanangizni xato kiritdingiz"
    
    
print(datetest("12/5/2006"))