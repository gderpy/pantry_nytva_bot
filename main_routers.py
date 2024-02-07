from aiogram import Router
from aiogram.filters.command import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def handle_start_cmd(message: Message):
    await message.answer(text="Проверка")

