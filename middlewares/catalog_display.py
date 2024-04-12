from typing import Awaitable, Callable, Any

from aiogram import BaseMiddleware
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from handlers.catalog.catalog_display import CatalogDisplay
from handlers.product_display.product_page import ProductPageBase


class CatalogDisplayMiddleware(BaseMiddleware):
    def __init__(self):
        self.catalog_display = CatalogDisplay()
        self.product_page = ProductPageBase()

    async def __call__(
            self,
            handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: dict[str, Any]
    ) -> Any:

        data["catalog_display"] = self.catalog_display
        data["product_page"] = self.product_page

        return await handler(event, data)