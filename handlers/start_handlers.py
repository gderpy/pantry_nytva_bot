import logging

from aiogram import Router, F
from aiogram.filters.command import CommandStart
from aiogram.types import Message, CallbackQuery

from keyboards import inline_admin_main_menu, inline_common_main_menu
from config.bot_config import ADMINS


router = Router()


@router.message(CommandStart())
@router.callback_query(F.data == "back_to_main_menu")
async def handle_start_cmd(msg: Message | CallbackQuery):

    logging.info(f"Пользователь - {msg.from_user.id}")

    if isinstance(msg, Message):
        if msg.from_user.id in ADMINS:
            text = "Главное меню администратора"
            kb = inline_admin_main_menu
        else:
            text = "Главное меню"
            kb = inline_common_main_menu

        await msg.delete()
        await msg.answer(text=text, reply_markup=kb)

    else:
        text = "Вы вернулись в главное меню администратора" \
            if msg.from_user.id in ADMINS else "Вы вернулись в главное меню"
        kb = inline_admin_main_menu \
            if msg.from_user.id in ADMINS else inline_common_main_menu

        await msg.message.edit_text(text=text, reply_markup=kb)
        await msg.answer()



