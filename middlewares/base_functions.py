from typing import Awaitable, Callable, Any

from aiogram import BaseMiddleware
from aiogram.types import Message

from handlers.sell_product.selling_product_basis import SellingProduct
from handlers.order_product.order_product_basis import OrderingProduct


class BaseFunctionsMiddleware(BaseMiddleware):
    def __init__(self):
        self.selling_product = SellingProduct()
        self.ordering_product = OrderingProduct()

    async def __call__(
            self,
            handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: dict[str, Any]
    ) -> Any:

        data["sell_product"] = self.selling_product
        data["order_product"] = self.ordering_product

        return await handler(event, data)

