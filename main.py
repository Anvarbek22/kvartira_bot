import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, types,F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from BUTTON.CAI_HISOB_BUTTON.button import*
from CONFIG.states import*
from SEARCH.filter import*
from DB.CAI_HISOB_DB.SQLITE.DB import*
from TOKEN.token import CAI_HISOB_TOKEN as TOKEN
from ADMIN.DB.SQLITE.DB import *
from CONFIG.config import *
import requests
dp = Dispatcher()
    

@dp.message(CommandStart())
async def start_command(message: types.Message,state:FSMContext):
    if userid(message.from_user.id):
        await state.set_state(logs.echo)
    elif test_user(message.from_user.id):
        await message.answer(f"Salom {message.from_user.full_name}!",reply_markup=dalete_acc)
        await state.set_state(logs.mails)
    else:    
        await message.reply(f"Salom {message.from_user.username}!",reply_markup=meynu())
        await state.set_state(logs.starts)

@dp.message(admin_los.starts)
async def del_get(message:types.Message):
    create_del2(message.text)
    await message.answer("Hisob o'chirildi")

@dp.message(admin_los.echo)
async def del_get(message:types.Message):
    create_del3(message.text)
    await message.answer("Echo botdagi client o'chirildi")


@dp.message(logs.starts)    
async def start_command(message: types.Message,state:FSMContext):
    text1=message.text
    if text1=="Singin":
        await message.answer(f"Telefon nomeringizni bering",reply_markup=menu)
        await state.set_state(logs.phones)

@dp.message(logs.phones)
async def echo_message(message: types.Message,state:FSMContext):
    try:
        data=message.contact.phone_number
        await message.answer("Ismingizni kiriting\n(Familya Ism)")
        await state.update_data({'phone':data})
        await state.set_state(logs.user_name)
    except: 
        await message.answer(text="Telefon nomeringizni bermasangiaz hisob ocha olmayman!")
        
@dp.message(logs.user_name)
async def echo_message(message: types.Message,state:FSMContext):
    text=message.text
    if username(text):
        await state.update_data({'ismi':text})
        await message.reply("Cmailingizni tanlang",reply_markup=Cmails(text.split()[0],text.split()[1]))
        await state.set_state(logs.Cmail)
    else:
        await message.answer("Ismingizni to'liq kiriting!")

@dp.message(logs.Cmail)
async def echo_message(message: types.Message,state:FSMContext):
    text=message.text
    a=cmail_filter(text)
    if text=="O'zim kiritaman":
        await message.reply("Cmailingizni kiriting\noxirida @cmail.uz deb yozing")            
        await state.set_state(logs.Cmail)
    elif a==True:
        await state.update_data({'cmail':text})
        await message.reply("Parolingizni kiriting\nkamida 8 ta belgi bo'lsin")
        await state.set_state(logs.Password)
    else:
        await message.answer(a)


@dp.message(logs.Password)
async def echo_message(message: types.Message,state:FSMContext):
    text=message.text
    if len(text)>=8:
        await state.update_data({'password':text})
        await message.reply("Tug'ilgan kuningizni kiriting:\nformat(kk/oo/yyyy)")
        await state.set_state(logs.date)
    else:
        await message.reply("Parolingiz kamida 8 belgi bolishi shart!")

@dp.message(logs.date)
async def echo_message(message: types.Message,state:FSMContext):
    text=message.text
    test=datetest(text)
    if test==True:
        await state.update_data({'date':text})
        await message.answer("tanlang",reply_markup=mael)
        await state.set_state(logs.yonalish)
    elif test=="Sizning yoshingiz kichik ekan\nsiz bu botdan foydalana olmaysiz":
        await message.answer(f"{test}")
        await state.set_state(logs.echo)
        create_add3(message.from_user.id)
    else: await message.answer(f"{test}")


@dp.message(logs.echo)
async def echo_message(message:types.Message):
    text1=message.text
    await message.answer(text=text1)





@dp.message(logs.yonalish)
async def echo_message(message:types.Message,state:FSMContext):
    text1=message.text
    data=await state.get_data()
    num=data.get('phone')
    name=data.get('ismi')
    date=data.get('date')
    cmail=data.get('cmail')
    password=data.get('password')
    await state.update_data({'mail':text1})
    await message.answer(text=f"Ism familiya: {name}\nTelefon no'mer: {num}\nCmail: {cmail}\nJins: {text1}\nTug'ilgan yil: {date}\nParol: {password}\n Maqulaysizmi?",reply_markup=yess)
    await state.set_state(logs.mail)
    
@dp.message(logs.mail)
async def echo_message(message:types.Message,state:FSMContext):
    text1=message.text
    if text1=="✅ Ha":
        data=await state.get_data()
        ids=message.from_user.id
        num=data.get('phone')
        name=data.get('ismi')
        date2=data.get('date')
        date=str(date2).replace("/","-")
        males=data.get('mail')
        cmail=data.get('cmail')
        password=data.get('password')
        data=requests.get(f"https://christapheruzb.pythonanywhere.com/login/add/{name}/{num}/{date}/{cmail}/{password}/{males}")
        print(data)
        create_add(ids,cmail,password)
        await message.answer(f"Salom {message.from_user.full_name}!",reply_markup=dalete_acc)
        await state.set_state(logs.mails)
    elif text1=="❌ Yo'q":
        await state.clear()
        await message.answer(f"Telefon nomeringizni bering",reply_markup=menu)
        await state.set_state(logs.phones)
    else: await message.answer("Bu commandani bajara olmayman")
    
@dp.message(logs.mails)
async def echo_message(message:types.Message,state:FSMContext):
    text=message.text
    if text=="🏗Access to the official site":
        await message.answer("Site: <a href='https://christapheruzb.pythonanywhere.com/'>GO</a>")
    elif text=="🧑‍💻 Admin bilan bog'lanish":
        await message.answer("👇👇👇",reply_markup=addmin)
    elif text=="🗑 Hisobni o'chirish":
        await message.answer("Hisobingizni o'chirasizmi\nEslatma: hisob barcha botlardan o'chib ketadi",reply_markup=yess)
    elif text=="del" and message.from_user.id == 5755772010:
        await message.answer(f"O'chirmoqchi bolgan hisobingizning telefon raqamini kiriting\n{db_search_del()}")
        await state.set_state(admin_los.starts)
    elif text=="echo" and message.from_user.id == 5755772010:
        a=""
        for i in create_read3():
            a+=f"{i[0]}\n"
        await message.answer(f"O'chirmoqchi bolgan hisobingizning  raqamini kiriting\n{a}")
        await state.set_state(admin_los.echo)
    elif text=="✅ Ha":
        create_del(str(message.from_user.id))
    elif text=="❌ Yo'q":
        await message.answer('Asosiy menyu',reply_markup=dalete_acc)
    else:await message.answer("Bu commandani bajara olmayman")
 
  
async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except:
        print("bot o'chdi")