from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest

from callback_factory.admin_callback import ProductPhotoCF

from fsm.base_fsm_data import FSMAddPhoto
from message_engine import MessageEngine
from sql.sql_engine import SQLEngine
from own_filters.admin_filters.photo_filters import PhotoCountFilter


router = Router()


def fsm_add_photo_kb(product_number: int, product_id: int, category_name: str, page: int):

    button_1 = InlineKeyboardButton(text="Отменить действие", callback_data=ProductCF(
                                            product_number=product_number,
                                            product_id=product_id,
                                            category=category_name,
                                            photo=True,
                                            from_page=page).pack())
    admin_kb = [
        [button_1]
    ]

    return InlineKeyboardMarkup(inline_keyboard=admin_kb)


def attach_photo_again(cd: str):

    button_1 = InlineKeyboardButton(text="Приложить фото снова", callback_data=cd)

    admin_kb = [
        [button_1]
    ]

    return InlineKeyboardMarkup(inline_keyboard=admin_kb)


def photos_attached(cd: int):

    button_1 = InlineKeyboardButton(text="Вернуться на страницу товара", callback_data=cd)

    admin_kb = [
        [button_1]
    ]

    return InlineKeyboardMarkup(inline_keyboard=admin_kb)


@router.callback_query(ProductPhotoCF.filter(F.product_id > 0))
async def add_product_photo(callback: CallbackQuery,
                            state: FSMContext,
                            message_engine: MessageEngine):

    message_engine.return_default_attrs()
    message_engine.saved_messages["first_message"] = callback.data

    callback_factory_obj = ProductPhotoCF.unpack(value=callback.data)
    product_number = callback_factory_obj.product_number
    product_id = callback_factory_obj.product_id
    category_name = callback_factory_obj.category
    current_page = callback_factory_obj.page

    text = "Вложите фото из своей галереи 📎"

    kb = fsm_add_photo_kb(product_number=product_number, product_id=product_id,
                          category_name=category_name, page=current_page)

    # Сохраняем message_id для дальнейшего использования
    message_engine.message_id = callback.message.edit_text(text=text).message_id
    message_engine.saved_messages[1] = {"product_number": product_number,
                                        "product_id": product_id,
                                        "category_name": category_name,
                                        "current_page": current_page}

    await callback.message.edit_text(text=text, reply_markup=kb)

    await state.set_state(FSMAddPhoto.photo)
    await callback.answer()


@router.message(FSMAddPhoto.photo)
async def taking_photo(message: Message,
                       state: FSMContext,
                       message_engine: MessageEngine,
                       sql_engine: SQLEngine):

    message_engine.count_photos += 1

    await message.delete()

    if message_engine.count_photos > 3:
        text = "Максимум можно вложить только 3 фото"
        await message.bot.edit_message_text(text=text,
                                            chat_id=message_engine.chat_id,
                                            message_id=message_engine.message_id,
                                            reply_markup=
                    attach_photo_again(cd=message_engine.saved_messages["first_message"]))

    if 0 < message_engine.count_photos < 4:

        text = "Фото загружено"
        if message_engine.count_photos == 1:
            text = f"Фото добавлено (+{message_engine.count_photos})"
        elif message_engine.count_photos > 1:
            text = f"Фото добавлены (+{message_engine.count_photos})"

        photo_id = message.photo[-2].file_id
        product_id = message_engine.saved_messages[1]["product_id"]

        await sql_engine.add_photo_id(photo_id, product_id)

        await message.bot.edit_message_text(text=text,
                                            chat_id=message_engine.chat_id,
                                            message_id=message_engine.message_id,
                                            reply_markup=photos_attached(
                                                cd=message_engine.product_page_id))










