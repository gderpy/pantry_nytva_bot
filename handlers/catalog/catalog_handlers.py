import logging

from aiogram import Router, F
from aiogram.types import CallbackQuery

from callback_factory.catalog_callbacks import CatalogCF
from keyboards import inline_catalog_menu, inline_catalog_menu_electronic_section
from sql.sql_engine import SQLEngine
from sql.models.categories_models import PhonesTable
from handlers.catalog.catalog_display import CatalogDisplay
from .catalog_utils import get_products_from_category, show_alert_if_products_are_missing

router = Router()


@router.callback_query(F.data == "view_products")
@router.callback_query(F.data == "view_products_again")
async def open_catalog(callback: CallbackQuery):
    await callback.message.edit_text(text="Выберите категорию товара",
                                     reply_markup=inline_catalog_menu)
    await callback.answer()


@router.callback_query(CatalogCF.filter(F.category == "electronic"))
async def open_electronic_section(callback: CallbackQuery):
    await callback.message.edit_text(text="Раздел электроники",
                                     reply_markup=inline_catalog_menu_electronic_section)
    await callback.answer()


@router.callback_query(CatalogCF.filter(F.category.in_({"phones", "cosmetic", "children_goods",
                                                        "tvs", "power_tools", "laptops"})))
@router.callback_query(CatalogCF.filter(F.paginator.in_({"next_page", "previous_page"})))
@get_products_from_category
@show_alert_if_products_are_missing
async def open_phones_section(callback: CallbackQuery,
                              category: str,
                              table_category: str,
                              products: dict,
                              current_page: int,
                              check: bool,
                              sql_engine: SQLEngine,
                              catalog_display: CatalogDisplay):

    logging.info(f"callback_data: {callback.data}")

    logging.info(f"category: {category}")  # catalog:phones:0:1:2:0
    logging.info(f"products: {products}")
    logging.info(f"current_page: {current_page}")

    if check is True:
        await callback.message.edit_text(
            text=table_category,
            reply_markup=catalog_display.display_category_products(products=products,
                                                                   category=category,
                                                                   current_page=current_page)
        )


@router.callback_query
async def catch_other_callbacks(callback: CallbackQuery):
    logging.info(f"callback_other: {callback.data}")
    await callback.answer()





