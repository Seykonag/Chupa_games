from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import user_commands, user_messages, task_proccess
from game import start_game
from data import Models

import asyncio
import os


async def main():
    load_dotenv()
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher(bot=bot)

    dp.include_routers(user_commands.router,
                       user_messages.router,
                       task_proccess.router,
                       start_game.router)

    await Models.database_start()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
