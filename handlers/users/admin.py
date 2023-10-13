import asyncio

from aiogram import types
from aiogram.types import Message, CallbackQuery,ReplyKeyboardRemove


from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(text="/admin")
async def get_all_users(message: Message):
    await message.answer("Baza tozalandi!")

@dp.message_handler(text="/all")
async def get_all_users(message: Message):
    users = await db.select_all_users()
    count = await db.count_users()
    for user in users:
        # print(user[3])
        user_id = user[0]
        user_full = user[1]
        user_usname = user[2]
        tg_id = user[3]
        msg = "\n".join([f"{user[1],user_id,user_full, user_usname, tg_id}"])
        await bot.send_message(chat_id=ADMINS[0], text=f"{msg}")
        await asyncio.sleep(0.05)
    await bot.send_message(chat_id=ADMINS[0], text=f"foydalanuvchi soni: {count} ta")
    



@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    for user in users:
        # print(user[3])
        user_id = user[3]
        await bot.send_message(chat_id=user_id, text="@SariqDev kanaliga obuna bo'ling!")
        await asyncio.sleep(0.05)