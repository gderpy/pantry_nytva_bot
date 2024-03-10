import os

from aiogram import Router, F
from aiogram.types import Message, FSInputFile, BufferedInputFile
from pathlib import Path

from admin_panel.excel_parser import ExcelParser
from message_engine import MessageEngine
from keyboards import inline_start_to_upload_data_from_excel_file

router = Router()

# "document": {
#       "file_id": "BQACAgIAAxkBAAIBqWXc7gqqTE1ZAjY3E-EXiLYNUXF4AAIISwACXEHpSr-Hu2LjvKeRNAQ",
#       "file_unique_id": "AgADCEsAAlxB6Uo",
#       "file_name": "Обновленный Excel-файл.xlsx",
#       "mime_type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
#       "file_size": 5453
#    }


@router.message(F.document.file_name.startswith("Ваш Excel-файл"))
async def attach_excel_file(message: Message, excel_parser: ExcelParser, message_engine: MessageEngine):

    excel_files_folder_path = Path.cwd() / "excel_files"
    # excel_files_folder_path: C:\Users\Юрий\excel_files
    file_names = os.listdir(excel_files_folder_path)
    # file_names: ['Excel-файл шаблон.xlsx', '__init__.py', 'Обновленный Excel-файл.xlsx']

    if "Обновленный Excel-файл.xlsx" in file_names:
        file_path = "Обновленный Excel-файл (2).xlsx"
    else:
        file_path = "Обновленный Excel-файл.xlsx"

    file_id = message.document.file_id

    await message.delete()
    await excel_parser.save_the_attached_file(message=message, file_id=file_id, file_path=file_path)

    await message.bot.edit_message_text(
        text=f"Файл сохранен",
        chat_id=message_engine.chat_id,
        message_id=message_engine.message_id,
        reply_markup=inline_start_to_upload_data_from_excel_file)




