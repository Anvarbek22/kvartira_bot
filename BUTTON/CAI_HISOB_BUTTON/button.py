from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from DB.CAI_KVARTIRA_DB.SQLITE.DB import *
from random import randint


menu=ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='✅ Ha',request_contact=True),KeyboardButton(text="❌ Yo'q")]],resize_keyboard=True)

yess=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='✅ Ha'),KeyboardButton(text="❌ Yo'q")]],resize_keyboard=True)

def Cmails(data1,data2):
    data3=randint(0,1000)
    res1=f"{data1}{data2}{data3}@cmail.uz"
    res2=f"{data2}{data1}{data3+45}@cmail.uz"
    res3=f"{data1}.{data2}{data3+1}@cmail.uz"
    res4="O'zim kiritaman"
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=res1)],[KeyboardButton(text=res2)],[KeyboardButton(text=res3)],[KeyboardButton(text=res4)]])


def db_search_button(ID):
    botses=[]
    botses.append([KeyboardButton(text='Make friends')])
    data=create_read()
    for i in data:
        if i[0]==str(ID):
            del botses[0]
    botses.append([KeyboardButton(text="Quiz bot")])
    return ReplyKeyboardMarkup(keyboard=botses,resize_keyboard=True)


def meynu():
    a=['Singin','Admin']
    build=[[KeyboardButton(text="Singin")],[KeyboardButton(text="🧑‍💻 Admin",url="https://t.me/anvarbek_197")]]
    return ReplyKeyboardMarkup(keyboard=build,resize_keyboard=True)

addmin=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='🧑‍💻 Admin',url="https://t.me/anvarbek_197")]])

dalete_acc=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='🏗Access to the official site')],[KeyboardButton(text="🧑‍💻 Admin bilan bog'lanish",)],[KeyboardButton(text="🗑 Hisobni o'chirish")]],resize_keyboard=True)
mael=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Male')],[KeyboardButton(text='Female')]],resize_keyboard=True)