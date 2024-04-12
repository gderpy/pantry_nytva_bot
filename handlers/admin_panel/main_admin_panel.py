import os

from aiogram import Router, F
from aiogram.types import CallbackQuery
from pathlib import Path

from callback_factory.admin_callback import AdminCF, ProductPhotoCF, Level
from keyboards.main_keyboard import inline_admin_panel


router = Router()


@router.callback_query(F.data == "admin_panel")
@router.callback_query(F.data == "back_to_admin_panel")
@router.callback_query(F.data == AdminCF(excel_parser=1, excel_parser_cancel_upload=1).pack())
async def handle_admin_panel(callback: CallbackQuery):

    excel_files_folder_path = Path.cwd() / "excel_files"
    file_names = os.listdir(excel_files_folder_path)

    if "Обновленный Excel-файл (2).xlsx" in file_names:
        os.remove(f"{excel_files_folder_path}/Обновленный Excel-файл (2).xlsx")

    await callback.message.edit_text(
        text="Панель администратора",
        reply_markup=inline_admin_panel
    )

