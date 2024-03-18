from typing import Awaitable, Callable, Any

from aiogram import BaseMiddleware
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from sql.sql_engine import SQLEngine


class SQLEngineMiddleware(BaseMiddleware):
    def __init__(self, sql_engine: SQLEngine):
        self.sql_engine = sql_engine

    async def __call__(
            self,
            handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: dict[str, Any]
    ) -> Any:

        data["sql_engine"] = self.sql_engine

        async with self.sql_engine.async_session() as session:
            data["session"] = session

        return await handler(event, data)

