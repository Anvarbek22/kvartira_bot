from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from CONFIG.infor import*
from SEARCH.search import*

BOG=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Bot bilan boglanish',url="https://t.me/CAI_hisob_bot")]])

def users_yon(ID):
    data=db_search_user_yon(ID)
    build=[]
    for i in data:
        build.append([KeyboardButton(text=f"{i[1]}-{i[0]}")])
    build.append([KeyboardButton(text="Universitetdan izlash")])
    return ReplyKeyboardMarkup(keyboard=build)

def users_uni(ID):
    data=db_search_user_uni(ID)
    build=[]
    for i in data:
        build.append([KeyboardButton(text=f"{i[1]}-{i[0]}")])
    build.append([KeyboardButton(text="Yo'nalishingizdan izlash")])
    return ReplyKeyboardMarkup(keyboard=build)





def users_url(data):
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Bog'lanish",url=data)]])


def university():
    build=[]
    for i in Tashkent:
        build.append([KeyboardButton(text=i['name'])])
    return ReplyKeyboardMarkup(keyboard=build,resize_keyboard=True)

def yonalish(data):
    build=[]
    for i in Tashkent2:
        if data==i['as_id']:
            build.append([KeyboardButton(text=i['name'])])
    build.append([KeyboardButton(text="Universitetdan izlash")])
    return ReplyKeyboardMarkup(keyboard=build,resize_keyboard=True)
