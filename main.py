import asyncio
import logging

import main_routers

from aiogram import Bot, Dispatcher

from config.bot_config import API_TOKEN
from middlewares import BaseFunctionsMiddleware
from middlewares.message_engine import MessageEngineMiddleware
from middlewares.sql_engine import SQLEngineMiddleware
from middlewares.excel_parser import ExcelParserMiddleware
from sql.sql_engine import SQLEngine



class MyBot:
    def __init__(self):
        self.bot = Bot(token=API_TOKEN, parse_mode="HTML")
        self.dp = Dispatcher()

        self.sql_engine = SQLEngine()

    async def on_startup(self):

        self.dp.update.middleware(BaseFunctionsMiddleware())
        self.dp.update.middleware(MessageEngineMiddleware())
        self.dp.update.middleware(SQLEngineMiddleware(sql_engine=self.sql_engine))
        self.dp.update.middleware(ExcelParserMiddleware())

        self.dp.include_router(main_routers.router)

        await self.bot.delete_webhook(drop_pending_updates=True)
        await self.dp.start_polling(self.bot)


if __name__ == "__main__":
    my_bot = MyBot()

    logging.getLogger().setLevel(logging.INFO)

    try:
        logging.info("Running a bot")
        asyncio.run(my_bot.on_startup())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot is disabled")


