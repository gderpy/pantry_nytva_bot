from aiogram import Router
from aiogram.filters.command import CommandStart
from aiogram.types import Message

from keyboards import inline_admin_main_menu, inline_common_main_menu
from config.bot_config import ADMINS


router = Router()


@router.message(CommandStart())
async def handle_start_cmd(message: Message):

    if message.from_user.id in ADMINS:
        text = "Главное меню администратора"
        kb = inline_admin_main_menu
    else:
        text = "Главное меню"
        kb = inline_common_main_menu

    await message.delete()
    await message.answer(text=text, reply_markup=kb)

