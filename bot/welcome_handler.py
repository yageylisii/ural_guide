from aiogram.filters import Command
from config import dp
from bot.text import WELCOME_TEXT
from bot.keyboard import welcome_keyboard
from bot.database import func_db

@dp.message(Command('start'))
async def start(message):
    user_id = message.from_user.id
    if await func_db.insert_data(user_id):
        await message.reply(WELCOME_TEXT, reply_markup=welcome_keyboard.welcome())
    else:
        await message.answer_sticker("CAACAgIAAxkBAAP5aPZKKgoXWwtK7AYbRafLjcOGxHoAAkKGAAJhDIFKQ_xjepzdfns2BA")
