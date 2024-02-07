import asyncio
import logging
import sys

import main_routers

from aiogram import Bot, Dispatcher

from config.bot_config import API_TOKEN
from config.log_config import FORMAT, FMT


class MyBot:
    def __init__(self):
        self.bot = Bot(token=API_TOKEN)
        self.dp = Dispatcher()

    async def on_startup(self):

        self.dp.include_router(main_routers.router)

        await self.bot.delete_webhook(drop_pending_updates=True)
        await self.dp.start_polling(self.bot)


if __name__ == "__main__":
    my_bot = MyBot()

    logging.basicConfig(format=FORMAT, datefmt=FMT, stream=sys.stdout, level="INFO")

    try:
        logging.info("Running a bot")
        asyncio.run(my_bot.on_startup())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot is disabled")


