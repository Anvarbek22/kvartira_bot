import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, types,F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from SEARCH.search import*
from CONFIG.state import*
from BUTTON.CAI_KVARTIRA_BUTTON.buttons import*
from TOKEN.token import CAI_KVARTIRA_TOKEN as TOKEN
# Replace 'TOKEN' with your actual bot token


dp = Dispatcher()

@dp.message(CommandStart())
async def start_command(message: types.Message,state:FSMContext):
    ids=message.from_user.id
    if db_search(ids):
        a=db_search_test(message.from_user.id)
        if a=="True":
            await message.answer(f"Sizni yo'nalishingizdagi talabalar",reply_markup=users_yon(ids))
            await state.set_state(logs.yonalish)
        else:
            await message.answer(f"O'qiyotgan universitetingizni tanlang",reply_markup=university())
            await state.set_state(logs.starts1)
    else:
        await message.answer(f"Sizda hisob yoq ekan CAI HISOB BOT botda hisob yarating",reply_markup=BOG)
        
  
@dp.message(logs.starts1)
async def start_command(message: types.Message,state:FSMContext):
    text=message.text
    for i in Tashkent:
        if i['name']==text:
            ids=i['id']
    await state.update_data({'uni_name':text})
    await message.answer(f"O'qiyotgan yonalishingizni tanlang",reply_markup=yonalish(ids))
    await state.set_state(logs.starts2)
    
    
    
    
@dp.message(logs.starts2)
async def start_command(message: types.Message,state:FSMContext):
    data=await state.get_data()
    texts=message.text
    ids=message.from_user.id
    name2=data.get("uni_name")
    url=message.from_user.url
    create_update(ids,name2,texts,url)
    await message.answer(f"Sizni yo'nalishingizdagi talabalar",reply_markup=users_yon(ids))
    await state.set_state(logs.yonalish)




@dp.message(logs.yonalish)
async def start_command(message: types.Message,state:FSMContext):
    texts=message.text
    if texts=="Universitetdan izlash":
        ids=message.from_user.id
        await message.answer(f"Sizni universitetingizdagi talabalar",reply_markup=users_uni(ids))
        await state.set_state(logs.universitet)
    else:    
        text=texts.split("-")
        ID=text[1]
        print(ID)
        data=search_user(ID)
        print(data) # https://t.me/anvarbek_197
        await message.answer(f"Talaba xaqida ma'lumot\n{data[0][1]}",reply_markup=users_url(data[0][0]))

@dp.message(logs.universitet)
async def start_command(message: types.Message,state:FSMContext):
    texts=message.text
    if texts=="Yo'nalishingizdan izlash":
        ids=message.from_user.id
        await message.answer(f"Sizni yo'nalishingizdagi talabalar",reply_markup=users_yon(ids))
        await state.set_state(logs.yonalish)
    else:    
        text=texts.split("-")
        ID=text[1]
        print(ID)
        data=search_user(ID)
        print(data) # https://t.me/anvarbek_197
        await message.answer(f"Talaba xaqida ma'lumot\n{data[0][1]}",reply_markup=users_url(data[0][0]))

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except:
        print("bot o'chdi")