import os

from aiogram import Router, F
from aiogram.types import CallbackQuery
from pathlib import Path

from callback_factory.admin_callback import AdminCF
from keyboards import inline_admin_cancel_upload_excel_file, inline_admin_main_menu
from message_engine import MessageEngine
from admin_panel.excel_parser import ExcelParser
from sql.sql_engine import SQLEngine

router = Router()


@router.callback_query(F.data == AdminCF(excel_parser_upload=1).pack())
async def press_button_to_upload_excel_file(callback: CallbackQuery, message_engine: MessageEngine):

    message_answer = callback.message.edit_text(
        text="Для выгрузки данных из Excel-файла просто приложите "
             "его через интерфейс телеграма 📎",
        reply_markup=inline_admin_cancel_upload_excel_file)

    message_engine.message_id = message_answer.message_id

    await message_answer

    print(callback.model_dump_json(indent=4, exclude_none=True))
    await callback.answer()


@router.callback_query(F.data == AdminCF(excel_parser=1, excel_parser_upload=1).pack())
async def parser_data_from_excel_to_tables(callback: CallbackQuery,
                                           excel_parser: ExcelParser):

    file_to_delete = Path.cwd() / "excel_files" / "Обновленный Excel-файл.xlsx"
    file_to_delete.unlink()

    current_path_to_old_name = Path.cwd() / "excel_files" / "Обновленный Excel-файл (2).xlsx"
    new_filename = "Обновленный Excel-файл.xlsx"
    new_path = current_path_to_old_name.with_name(new_filename)
    current_path_to_old_name.rename(new_path)

    current_path_to_new_file = Path.cwd() / "excel_files" / "Обновленный Excel-файл.xlsx"

    await excel_parser.upload_data_from_excel_file_to_models(current_path_to_new_file)
    await callback.answer()
    await callback.message.edit_text(
        text="Данные внесены в каталог!",
        reply_markup=inline_admin_main_menu
    )











