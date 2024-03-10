from typing import Awaitable, Callable, Any

from aiogram import BaseMiddleware
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from handlers.catalog.catalog_display import CatalogDisplay


class CatalogDisplayMiddleware(BaseMiddleware):
    def __init__(self):
        self.catalog_display = CatalogDisplay()

    async def __call__(
            self,
            handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: dict[str, Any]
    ) -> Any:

        data["catalog_display"] = self.catalog_display

        return await handler(event, data)