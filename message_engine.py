import logging

from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardMarkup


class MessageEngine:
    __chat_id: int
    bot: Bot

    def __init__(self):
        self.event: Message | CallbackQuery | None = None
        self.message_id: int | None = None

    @property
    def chat_id(self):
        return self.__chat_id

    @chat_id.setter
    def chat_id(self, value):
        self.__chat_id = value
        logging.info(f"self.__chat_id = {self.__chat_id}")

    async def edit_message(self, text: str, keyboard: InlineKeyboardMarkup | None):

        if isinstance(self.event, Message):
            message = self.event
            await message.bot.edit_message_text(text=text,
                                                chat_id=self.chat_id,
                                                message_id=self.message_id,
                                                reply_markup=keyboard)

        elif isinstance(self.event, CallbackQuery):
            callback = self.event
            await callback.message.edit_text(text=text,
                                             reply_markup=keyboard)

    def return_default_attrs(self):
        self.event = None
        self.message_id = None

