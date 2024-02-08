from typing import Awaitable, Callable, Any

from aiogram import BaseMiddleware
from aiogram.types import Message

from message_engine import MessageEngine


class MessageEngineMiddleware(BaseMiddleware):
    def __init__(self):
        self.message_engine = MessageEngine()

    async def __call__(
            self,
            handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: dict[str, Any]
    ) -> Any:

        self.message_engine.bot = data.get("bot")
        self.message_engine.chat_id = data.get("event_chat").id

        data["message_engine"] = self.message_engine

        return await handler(event, data)

