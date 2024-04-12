import logging

from aiogram import F, Router
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from aiogram.exceptions import TelegramBadRequest
from sqlalchemy.ext.asyncio import AsyncSession
from functools import wraps

from sql.sql_engine import SQLEngine
from handlers.product_display.product_page import ProductPageBase
from handlers.catalog.catalog_utils import photo_upload_check
from message_engine import MessageEngine


router = Router()


# def product_menu_kb(category: str, page: int, admin: bool, product_id: int,
#                     product_number: int, category_name: str, current_page: int):
#
#     button_1 = InlineKeyboardButton(text="Добавить в корзину", callback_data="add_to_cart")
#     button_2 = InlineKeyboardButton(text="Назад",
#                                     callback_data=CatalogCF(category=category, page=page).pack())
#     button_3 = InlineKeyboardButton(text="Добавить фото", callback_data=ProductPhotoCF(
#                                             product_id=product_id,
#                                             product_number=product_number,
#                                             category=category_name,
#                                             page=current_page).pack())
#     button_4 = InlineKeyboardButton(text="Назад",
#                                     callback_data=CatalogCF(category=category,
#                                                             page=page, photo=True).pack())
#
#     user_kb = [
#         [button_1],
#         [button_2]
#     ]
#
#     admin_kb = [
#         [button_3],
#         [button_4]
#     ]
#
#     general_kb = admin_kb if admin else user_kb
#
#     return InlineKeyboardMarkup(inline_keyboard=general_kb)
#
#
# def photo_switch(cd_back_button: str | CatalogCF,
#                  cd_display_photo: str,
#                  photo_number: int,
#                  number_of_photos: int):
#
#     button_1 = InlineKeyboardButton(text="Фото ⏩", callback_data=cd_display_photo)
#     button_2 = InlineKeyboardButton(text="Назад", callback_data=cd_back_button)
#     button_3 = InlineKeyboardButton(text="Добавить в корзину", callback_data="add_to_cart")
#     button_4 = InlineKeyboardButton(text="⏪ Фото ⏩", callback_data=cd_display_photo)
#     button_5 = InlineKeyboardButton(text="⏪ Фото", callback_data=cd_display_photo)
#     button_6 = InlineKeyboardButton(text="⏪", callback_data=cd_display_photo)
#     button_7 = InlineKeyboardButton(text="⏩", callback_data=cd_display_photo)
#     button_8 = InlineKeyboardButton(text="Фото", callback_data=cd_display_photo)
#
#     photo_number += 1
#
#     if number_of_photos == 1:
#         kb = [
#             [button_3],
#             [button_2]
#         ]
#
#     elif photo_number == 1 and number_of_photos > 1:
#         kb = [
#             [button_1],
#             [button_3],
#             [button_2]
#         ]
#
#     elif photo_number == number_of_photos:
#         kb = [
#             [button_5],
#             [button_3],
#             [button_2]
#         ]
#
#     elif photo_number == 2 and number_of_photos == 3:
#         kb = [
#             [button_6, button_7],
#             [button_3],
#             [button_2]
#         ]
#
#     return InlineKeyboardMarkup(inline_keyboard=kb)
#
#
# @router.callback_query(ProductCF.filter(F.product_number > 0))
# async def open_a_specific_product(callback: CallbackQuery,
#                                   product_page: ProductPage,
#                                   session: AsyncSession,
#                                   message_engine: MessageEngine,
#                                   sql_engine: SQLEngine,
#                                   callback_factory: ProductCF,
#                                   **kwargs):
#
#     print(f"callback_data: {callback.data}, "
#           f"callback_factory: {callback_factory}")

    # Первая страница каталога-товар с фото
    # callback_data - product:phones:1:1:205:0:1:1
    # callback_factory - category='phones'
    #                    product_number=1
    #                    from_page=1
    #                    product_id=205
    #                    photo_number=0
    #                    photo=True
    #                    product_with_photo=True

    # Первая страница каталога-товар без фото
    # callback_data - product:phones:6:1:210:0:1:0
    # callback_factory - category='phones'
    #                    product_number=6
    #                    from_page=1
    #                    product_id=210
    #                    photo_number=0
    #                    photo=True
    #                    product_with_photo=False

    # cf = callback_factory
    # photo_number = cf.photo_number
    #
    # # Получаем текстовое описание товара
    # product_info = await product_page.get_product_info(category_name=cf.category,
    #                                                    session=session,
    #                                                    product_id=cf.product_id)
    #
    # # Проверяем есть ли фото у товара
    # check = await sql_engine.get_photos_from_table(product_id=cf.product_id)
    # print(f"check: {check}")
    # category_name = product_page.categories_dict.get(cf.category)[0]
    #
    # if check:
    #     caption = product_info
    #     photo = check[photo_number]
    #
    #     callback_factory.photo_number += 1
    #
    #     previous_cd: CatalogCF = message_engine.bot_sections.catalog_section.callback_data
    #     previous_cd.product_with_photo = True
    #
    #     kb = photo_switch(
    #         cd_back_button=previous_cd.pack(),
    #         cd_display_photo=callback_factory.pack(),
    #         photo_number=photo_number,
    #         number_of_photos=len(check)
    #     )
    #
    #     if cf.product_with_photo is True:
    #
    #         if photo_number == 0:
    #
    #             await callback.bot.delete_message(
    #                 chat_id=message_engine.chat_id,
    #                 message_id=message_engine.bot_sections.catalog_section.message_id
    #             )
    #
    #             await callback.bot.send_photo(
    #                 chat_id=message_engine.chat_id,
    #                 photo=photo,
    #                 reply_markup=kb,
    #                 caption=caption
    #             )
    #
    #         elif photo_number + 1 == len(check) or photo_number + 1 == 2 and len(check) == 3:
    #
    #             await callback.message.edit_media(
    #                 media=InputMediaPhoto(media=photo, caption=caption),
    #                 reply_markup=kb
    #                 )
    #
    #
    # else:
    #
    #     await callback.message.edit_text(
    #         text=product_info,
    #         reply_markup=product_menu_kb(category=cf.category,
    #                                      page=cf.from_page,
    #                                      admin=cf.photo,
    #                                      product_id=cf.product_id,
    #                                      product_number=cf.product_number,
    #                                      category_name=category_name,
    #                                      current_page=cf.from_page)
    #      )
    #
    # await callback.answer()

