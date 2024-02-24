import logging

from aiogram import F, Router
from aiogram.types import CallbackQuery

from callback_factory.admin_callback import AdminCF
from admin_panel.excel_parser import ExcelParser
from keyboards import inline_hide_excel_file
from sql.sql_engine import SQLEngine
from sql.models import SellTable, OrderTable


router = Router()


@router.callback_query(F.data == AdminCF(excel_parser=1).pack())
async def handle_downloading_excel_file(callback: CallbackQuery,
                                        excel_parser: ExcelParser):

    await callback.answer()
    await excel_parser.download_excel_file()

    await callback.bot.send_document(
        chat_id=excel_parser.chat_id,
        document=excel_parser.excel_file(),
        caption="Файл Excel",
        reply_markup=inline_hide_excel_file
    )


@router.callback_query(F.data == AdminCF(excel_parser=1, excel_parser_download=1).pack())
async def hide_excel_file(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer()
