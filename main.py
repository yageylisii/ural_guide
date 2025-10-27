import asyncio
from config import bot, dp
from bot import welcome_handler, private_handlers

from bot.database.core import init_db
# from bot import callback_hand
# from bot.handlers import boxes_handlers, handlers_business, handlers_private, lucky_bomb_handlers, handlers_tower
# from bot.send_gifts import sender

async def main():
    await init_db()
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())