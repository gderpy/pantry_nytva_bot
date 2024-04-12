from aiogram.filters import BaseFilter
from aiogram.types import Message

from message_engine import MessageEngine


class PhotoCountFilter(BaseFilter):
    def __init__(self, count_photos: int):
        self.count_photos = count_photos

    async def __call__(self, message: Message, message_engine: MessageEngine) -> bool:

        if self.count_photos == 1:
            message_engine.saved_messages["bot_message"] = {1: message.message_id}
            return True

        elif self.count_photos > 1:

            await message.bot.delete_message(
                chat_id=message_engine.chat_id,
                message_id=message_engine.saved_messages["bot_message"][1])
            message_engine.saved_messages["bot_message"][1] = message.message_id
            return True

        else:
            return False

