from sqlalchemy.ext.asyncio import AsyncSession

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import (CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup,
                           Message, InputMediaPhoto)

from fsm.base_fsm_data import FSMAddPhoto
from sql.sql_engine import SQLEngine
from message_engine import MessageEngine
from handlers.product_display.product_page import ProductPageBase
from handlers.catalog.catalog_display import CatalogDisplay
from keyboards.catalog_kb import categories, categories_dict
from keyboards.catalog_kb import (ChoosingCategory, CategoryPage, ProductPage,
                                  choosing_category_keyboard, Photo, PhotoAction)

router = Router()


@router.callback_query(ChoosingCategory.filter(F.user_type.in_({"admin", "user"})))
async def open_category_choosing(callback: CallbackQuery,
                                 callback_factory: ChoosingCategory,
                                 *args, **kwargs):
    kb: list[list[InlineKeyboardButton]] = (
        choosing_category_keyboard(user_type=callback_factory.user_type))["general_kb"]

    if callback_factory.user_type == "user":
        text = "Выберите категорию товара"
        back_button = InlineKeyboardButton(text="Вернуться в главное меню 📲",
                                           callback_data="back_to_main_menu")

    elif callback_factory.user_type == "admin":
        text = "Для работы с товаром, выберите категорию товара"
        back_button = InlineKeyboardButton(text="Вернуться в админ-панель 📲",
                                           callback_data="back_to_admin_panel")

    kb.append([back_button])

    reply_markup_kb = InlineKeyboardMarkup(inline_keyboard=kb)

    await callback.message.edit_text(text=text, reply_markup=reply_markup_kb)
    await callback.answer(text=callback.data)


@router.callback_query(CategoryPage.filter(F.category == "electronic"))
async def open_category_section(callback: CallbackQuery,
                                callback_factory: CategoryPage):
    kb: list[list[InlineKeyboardButton]] = (
        choosing_category_keyboard(user_type=callback_factory.user_type))["electronic_category_kb"]

    if callback_factory.user_type == "user":

        back_button = InlineKeyboardButton(
            text="Вернуться к выбору категории",
            callback_data=ChoosingCategory(user_type="user").pack())

    elif callback_factory.user_type == "admin":

        back_button = InlineKeyboardButton(
            text="Вернуться к выбору категории",
            callback_data=ChoosingCategory(user_type="admin").pack()
        )

    kb.append([back_button])

    reply_markup_kb = InlineKeyboardMarkup(inline_keyboard=kb)

    await callback.message.edit_text(
        text="Электроника",
        reply_markup=reply_markup_kb
    )

    await callback.answer(text=callback.data)


@router.callback_query(CategoryPage.filter(F.category.in_(categories)))
async def open_category_page(callback: CallbackQuery,
                             callback_factory: CategoryPage,
                             sql_engine: SQLEngine,
                             catalog_display: CatalogDisplay,
                             message_engine: MessageEngine,
                             product_page: ProductPageBase,
                             *args, **kwargs):

    print(f"callback_category: {callback.data}")
    product_page.set_keyboard(catalog_callback_factory=callback_factory)

    if callback_factory.paginator == "next_page":
        callback_factory.current_page += 1
    elif callback_factory.paginator == "previous_page":
        callback_factory.current_page -= 1

    user_type = callback_factory.user_type

    table_category = categories_dict.get(callback_factory.category)
    current_page = callback_factory.current_page

    products = await sql_engine.display_a_product_of_a_specific_category(category=table_category)
    text = table_category if user_type == "user" else "Выберите товар для редактирования"

    if len(products) == 0:
        return await callback.answer(
            text="В данной категории товары отсутствуют",
            show_alert=True
        )
    else:

        catalog_keyboard = await catalog_display.display_category_products(
            user_type=user_type,
            products=products,
            category=callback_factory.category,
            current_page=current_page)

        callback_message_edit_text = callback.message.edit_text(
            text=text,
            reply_markup=catalog_keyboard
        )

        callback_message_answer = callback.message.answer(
            text=text,
            reply_markup=catalog_keyboard
        )

        if callback_factory.return_after_photo is False:
            message_engine.previous_message_id = callback_message_edit_text.message_id
            await callback_message_edit_text
        else:
            await callback.message.delete()
            message_engine.previous_message_id = None
            await callback_message_answer

    await callback.answer()


@router.callback_query(ProductPage.filter(
    (F.user_type.in_({"user", "admin"})) & (F.number_of_photos > 0)))
async def open_product_page_with_several_photos(callback: CallbackQuery,
                                                callback_factory: ProductPage,
                                                sql_engine: SQLEngine,
                                                message_engine: MessageEngine,
                                                product_page: ProductPageBase,
                                                session: AsyncSession,
                                                *args, **kwargs):
    print(callback_factory)
    print(f"product_callback: {callback.data}")
    first_press = callback_factory.first_press
    callback_factory.first_press = False

    product_page.set_keyboard(product_callback_factory=callback_factory)

    photos = await sql_engine.get_photos_from_table(callback_factory.product_id)
    text = await product_page.get_product_info(category_name=callback_factory.category,
                                               session=session,
                                               product_id=callback_factory.product_id)

    await product_page.product_page_answer(callback,
                                           text,
                                           photos=photos,
                                           previous_message_id=message_engine.previous_message_id,
                                           chat_id=message_engine.chat_id,
                                           first_press=first_press)

    await callback.answer()


@router.callback_query(ProductPage.filter(
    (F.user_type.in_({"user", "admin"})) & (F.number_of_photos == 0)))
async def open_product_page_without_photo(callback: CallbackQuery,
                                          product_page: ProductPageBase,
                                          callback_factory: ProductPage,
                                          session: AsyncSession):

    product_page.set_keyboard(product_callback_factory=callback_factory)
    text = await product_page.get_product_info(category_name=callback_factory.category,
                                               session=session,
                                               product_id=callback_factory.product_id)

    await product_page.product_page_answer(callback, text)
    await callback.answer()


@router.callback_query(Photo.filter(F.photo_action == PhotoAction.add_photo))
async def add_photo_to_product(callback: CallbackQuery,
                               state: FSMContext,
                               product_page: ProductPageBase,
                               message_engine: MessageEngine):

    text = "Вложите фото из своей галереи 📎"
    message_answer, message_engine.previous_message_id = (
        product_page.photo_addition_process(callback, text))

    await message_answer
    await state.set_state(FSMAddPhoto.photo)
    await callback.answer("Добавление фото")


@router.message(FSMAddPhoto.photo)
async def the_photo_has_been_added(message: Message,
                                   state: FSMContext,
                                   message_engine: MessageEngine):

    message_engine.count_photos += 1

    text = "Добавляем?"

    await message.bot.delete_message(
        chat_id=message_engine.chat_id,
        message_id=message_engine.previous_message_id
    )

    await message.answer(
        text=text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Добавить", callback_data="add_this_photo"),
             InlineKeyboardButton(text="Отмена", callback_data="other_photo")]
        ])
    )





