from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter
from sqlalchemy.ext.asyncio import AsyncSession

from handlers.sell_product.selling_product_basis import SellingProduct
from message_engine import MessageEngine
from fsm.base_fsm_data import FSMSellingProduct
from keyboards import inline_sell_menu, inline_sell_menu_end
from sql.models.base import SellTable
from sql.sql_engine import SQLEngine


router = Router()


@router.callback_query(F.data == "sell_a_product")
async def handle_selling_product(callback: CallbackQuery,
                                  state: FSMContext,
                                  sell_product: SellingProduct,
                                  message_engine: MessageEngine):

    # Сброс к первоначальным данным
    sell_product.default_properties()

    text = sell_product.basic_template()

    # Сохраняем message_id для дальнейшего использования
    message_engine.message_id = callback.message.edit_text(text=text).message_id

    await callback.message.edit_text(text=text, reply_markup=inline_sell_menu)
    await state.set_state(FSMSellingProduct.name)
    await callback.answer()


@router.message(StateFilter(FSMSellingProduct.name))
async def set_name_offer_product(message: Message,
                                 state: FSMContext,
                                 sell_product: SellingProduct,
                                 message_engine: MessageEngine):

    # Присваиваем тип апдейта
    message_engine.event = message

    sell_product.name = message.text
    text = sell_product.basic_template()

    await message.delete()
    await message_engine.edit_message(text=text, keyboard=inline_sell_menu)
    await state.set_state(FSMSellingProduct.price)


@router.message(StateFilter(FSMSellingProduct.price))
async def set_price_offer_product(message: Message,
                                  sell_product: SellingProduct,
                                  message_engine: MessageEngine):

    sell_product.price = message.text
    text = sell_product.basic_template()

    await message.delete()
    await message_engine.edit_message(text=text, keyboard=inline_sell_menu_end)


@router.callback_query(F.data == "send_product_data")
async def handle_sent_data(callback: CallbackQuery,
                           sell_product: SellingProduct,
                           message_engine: MessageEngine,
                           sql_engine: SQLEngine):

    message_engine.event = callback
    text = sell_product.basic_template()

    data = {"name": sell_product.name, "price": int(sell_product.price)}

    await sql_engine.insert_objects(model=SellTable, data=data)

    await message_engine.edit_message(text=text, keyboard=inline_sell_menu)
    await callback.answer()









