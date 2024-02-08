from typing import Awaitable, Callable, Any

from aiogram import BaseMiddleware
from aiogram.types import Message

from handlers.offering_product.offering_product_basis import OfferingProduct


class OfferingProductMiddleware(BaseMiddleware):
    def __init__(self):
        self.offering_product = OfferingProduct()

    async def __call__(
            self,
            handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: dict[str, Any]
    ) -> Any:
        data["offer_product"] = self.offering_product
        return await handler(event, data)

