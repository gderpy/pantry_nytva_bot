import logging

from aiogram import F, Router
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from sqlalchemy.ext.asyncio import AsyncSession


from callback_factory.catalog_callbacks import CatalogCF, ProductCF
from sql.sql_engine import SQLEngine
from handlers.product_display.product_page import ProductPage


router = Router()


def product_menu_kb(category: str, page: int):

    button_1 = InlineKeyboardButton(text="Добавить в корзину", callback_data="add_to_cart")
    button_2 = InlineKeyboardButton(text="Назад",
                                    callback_data=CatalogCF(category=category, page=page).pack())

    return InlineKeyboardMarkup(inline_keyboard=[
        [button_1],
        [button_2]
    ])


@router.callback_query(ProductCF.filter(F.product_number > 0))
async def open_a_specific_product(callback: CallbackQuery,
                                  product_page: ProductPage,
                                  session: AsyncSession):
    # product:phones:1

    # product:phones:6:Tecno POVA 5 256 ГБ чрн.:180

    callback_factory_obj = ProductCF.unpack(value=callback.data)
    category_name: str = callback_factory_obj.category  # phones
    current_page: int = callback_factory_obj.from_page
    product_id: int = callback_factory_obj.product_id

    product_info = await product_page.get_product_info(category_name, session, product_id)

    await callback.message.edit_text(
        text=product_info,
        reply_markup=product_menu_kb(category=category_name, page=current_page)
    )

