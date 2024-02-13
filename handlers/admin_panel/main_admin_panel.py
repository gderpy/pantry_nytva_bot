from aiogram import Router, F
from aiogram.types import CallbackQuery

from callback_factory.admin_callback import AdminCF
from keyboards.main_keyboard import inline_admin_panel


router = Router()


@router.callback_query(F.data == "admin_panel")
async def handle_admin_panel(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Панель администратора",
        reply_markup=inline_admin_panel
    )

