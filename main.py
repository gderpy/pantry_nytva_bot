import asyncio
import logging
import sys

import main_routers

from aiogram import Bot, Dispatcher
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config.bot_config import API_TOKEN
from config.db_config import postgres_url
from middlewares.offer import OfferingProductMiddleware
from middlewares.message_engine import MessageEngineMiddleware


class MyBot:
    def __init__(self):
        self.bot = Bot(token=API_TOKEN, parse_mode="HTML")
        self.dp = Dispatcher()

        self.engine = create_async_engine(url=postgres_url, echo=True)
        self.async_session = async_sessionmaker(bind=self.engine, expire_on_commit=False)

    async def on_startup(self):

        self.dp.update.middleware(OfferingProductMiddleware())
        self.dp.update.middleware(MessageEngineMiddleware())

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


