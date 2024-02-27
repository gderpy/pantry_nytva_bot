from typing import Awaitable, Callable, Any

from aiogram import BaseMiddleware
from aiogram.types import Message

from handlers.base_functions.base_functions_engine import BaseFunctionsEngine


class BaseFunctionsMiddleware(BaseMiddleware):
    def __init__(self):
        self.base_functions = BaseFunctionsEngine()

    async def __call__(
            self,
            handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: dict[str, Any]
    ) -> Any:

        data["base_function"] = self.base_functions

        return await handler(event, data)

