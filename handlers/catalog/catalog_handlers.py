from aiogram import Router, F
from aiogram.types import CallbackQuery

from callback_factory.catalog_callbacks import CatalogCF
from keyboards import inline_catalog_menu, inline_catalog_menu_electronic_section

router = Router()


@router.callback_query(F.data == "view_products")
@router.callback_query(F.data == "view_products_again")
async def open_catalog(callback: CallbackQuery):
    await callback.message.edit_text(text="Выберите категорию товара",
                                     reply_markup=inline_catalog_menu)
    await callback.answer()


@router.callback_query(F.data == CatalogCF(electronic=1).pack())
async def open_electronic_section(callback: CallbackQuery):
    await callback.message.edit_text(text="Раздел электроники",
                                     reply_markup=inline_catalog_menu_electronic_section)
    await callback.answer()

