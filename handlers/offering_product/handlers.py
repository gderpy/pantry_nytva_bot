from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter

from handlers.offering_product.offering_product_basis import OfferingProduct
from message_engine import MessageEngine
from fsm.fsm_offering_product import FSMOfferingProduct
from keyboards import inline_offer_menu, inline_offer_menu_end


router = Router()


@router.callback_query(F.data == "offer_a_product")
async def handle_offering_product(callback: CallbackQuery,
                                  state: FSMContext,
                                  offer_product: OfferingProduct,
                                  message_engine: MessageEngine):

    # Сброс к первоначальным данным
    offer_product.default_properties()

    text = offer_product.basic_template()

    # Сохраняем message_id для дальнейшего использования
    message_engine.message_id = callback.message.edit_text(text=text).message_id

    await callback.message.edit_text(text=text, reply_markup=inline_offer_menu)
    await state.set_state(FSMOfferingProduct.name)
    await callback.answer()


@router.message(StateFilter(FSMOfferingProduct.name))
async def set_name_offer_product(message: Message,
                                 state: FSMContext,
                                 offer_product: OfferingProduct,
                                 message_engine: MessageEngine):

    # Присваиваем тип апдейта
    message_engine.event = message

    offer_product.name = message.text
    text = offer_product.basic_template()

    await message.delete()
    await message_engine.edit_message(text=text, keyboard=inline_offer_menu)
    await state.set_state(FSMOfferingProduct.price)


@router.message(StateFilter(FSMOfferingProduct.price))
async def set_price_offer_product(message: Message,
                                  offer_product: OfferingProduct,
                                  message_engine: MessageEngine):

    offer_product.price = message.text
    text = offer_product.basic_template()

    await message.delete()
    await message_engine.edit_message(text=text, keyboard=inline_offer_menu_end)


@router.callback_query(F.data == "send_product_data")
async def handle_sent_data(callback: CallbackQuery,
                           offer_product: OfferingProduct,
                           message_engine: MessageEngine):

    message_engine.event = callback
    text = offer_product.basic_template()

    await message_engine.edit_message(text=text, keyboard=inline_offer_menu)
    await callback.answer()









