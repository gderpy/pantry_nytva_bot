import logging

from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter
from aiogram.exceptions import TelegramBadRequest

from message_engine import MessageEngine
from fsm.base_fsm_data import FSMSellProduct, FSMOrderProduct
from keyboards import (inline_base_sell_func_menu, inline_base_sell_func_menu_end,
                       inline_base_order_func_menu, inline_base_order_func_menu_end)
from sql.models import SellsTable, OrdersTable
from sql.sql_engine import SQLEngine
from handlers.base_functions.base_functions_engine import BaseFunctionsEngine
from handlers.base_functions.utils import (define_type_update, handle_fsm_sell_and_offer_product,
                                           correct_price, send_base_func_data)


router = Router()


@router.callback_query(F.data.in_({"sell_a_product", "order_a_product"}))
async def handle_base_functions(callback: CallbackQuery,
                                state: FSMContext,
                                base_function: BaseFunctionsEngine,
                                message_engine: MessageEngine):

    """Кнопка 'Продать'/'Заказать'"""

    # Сброс к первоначальным данным
    base_function.default_properties()

    # Определяем запрос от пользователя: какую кнопку он нажал 'Продажа'/'Заявка'
    # obj_text: Объект, который содержит текст для процесса FSM
    # fsm_arg: Объект FSM с состояниями 'Продажа'/'Заявка'
    
    if callback.data == "sell_a_product":
        obj_text = base_function.bot_text.selling_text
        fsm_arg = FSMSellProduct.name
    elif callback.data == "order_a_product":
        obj_text = base_function.bot_text.ordering_text
        fsm_arg = FSMOrderProduct.name

    text = base_function.basic_template(obj_text=obj_text)
        
    # Сохраняем message_id для дальнейшего использования
    message_engine.message_id = callback.message.edit_text(text=text).message_id

    await callback.message.edit_text(text=text, reply_markup=inline_base_sell_func_menu)
    await state.set_state(fsm_arg)
    await callback.answer()


@router.message(StateFilter(FSMSellProduct.name))
async def set_name_sell_product(message: Message,
                                state: FSMContext,
                                base_function: BaseFunctionsEngine,
                                message_engine: MessageEngine):

    """Продать товар - название товара"""

    define_type_update(update=message, message_engine=message_engine)
    base_function.name = message.text

    await handle_fsm_sell_and_offer_product(message,
                                            state,
                                            base_function,
                                            message_engine,
                                            base_function.bot_text.selling_text,
                                            FSMSellProduct.price,
                                            keyboard=inline_base_sell_func_menu)


@router.message(StateFilter(FSMOrderProduct.name))
async def set_name_order_product(message: Message,
                                 state: FSMContext,
                                 base_function: BaseFunctionsEngine,
                                 message_engine: MessageEngine):

    """Заказать товар - название товара"""

    define_type_update(update=message, message_engine=message_engine)
    base_function.name = message.text

    await handle_fsm_sell_and_offer_product(message,
                                            state,
                                            base_function,
                                            message_engine,
                                            base_function.bot_text.ordering_text,
                                            next_state=FSMOrderProduct.contact,
                                            keyboard=inline_base_order_func_menu)


@router.message(StateFilter(FSMSellProduct.price))
async def set_price_sell_product(message: Message,
                                 state: FSMContext,
                                 base_function: BaseFunctionsEngine,
                                 message_engine: MessageEngine):

    """Продать товар - стоимость товара"""

    try:
        if correct_price(text_price=message.text) == "Неверный формат стоимости. Отправьте повторно":
            await message.delete()
            await state.set_state(FSMSellProduct.price)
            await message_engine.edit_message(text="<b><i>Неверный формат стоимости. Отправьте повторно</i></b>",
                                              keyboard=inline_base_sell_func_menu)

        else:
            base_function.price = correct_price(message.text)

            await handle_fsm_sell_and_offer_product(message,
                                                    state,
                                                    base_function,
                                                    message_engine,
                                                    base_function.bot_text.selling_text,
                                                    next_state=FSMSellProduct.contact,
                                                    keyboard=inline_base_sell_func_menu)
    except TelegramBadRequest as e:
        logging.info("Пользователь отправляет неверный формат стоимости по несколько раз")
        await message_engine.edit_message(text="<b><i>До сих пор неверно!</i></b>",
                                          keyboard=inline_base_sell_func_menu)


@router.message(StateFilter(FSMOrderProduct.contact))
async def set_contact_order_product(message: Message,
                                    state: FSMContext,
                                    base_function: BaseFunctionsEngine,
                                    message_engine: MessageEngine):

    """Заказать товар - оставить контакты"""

    base_function.contact = message.text

    await handle_fsm_sell_and_offer_product(message,
                                            state,
                                            base_function,
                                            message_engine,
                                            base_function.bot_text.ordering_text,
                                            next_state=None,
                                            keyboard=inline_base_order_func_menu_end)


@router.message(StateFilter(FSMSellProduct.contact))
async def set_contact_sell_product(message: Message,
                                   state: FSMContext,
                                   base_function: BaseFunctionsEngine,
                                   message_engine: MessageEngine):

    """Продать товар - оставить контакты"""

    base_function.contact = message.text

    await handle_fsm_sell_and_offer_product(message,
                                            state,
                                            base_function,
                                            message_engine,
                                            base_function.bot_text.selling_text,
                                            next_state=None,
                                            keyboard=inline_base_sell_func_menu_end)


@router.callback_query(F.data == "send_sell_product_data")
async def handle_sent_sell_data(callback: CallbackQuery,
                                base_function: BaseFunctionsEngine,
                                message_engine: MessageEngine,
                                sql_engine: SQLEngine):

    print(f"мы тут - sell - {base_function.price}")

    obj_text = base_function.bot_text.selling_text

    await send_base_func_data(callback,
                              base_function,
                              message_engine,
                              sql_engine,
                              obj_text,
                              SellsTable,
                              inline_base_sell_func_menu)


@router.callback_query(F.data == "send_order_product_data")
async def handle_sent_order_data(callback: CallbackQuery,
                                 base_function: BaseFunctionsEngine,
                                 message_engine: MessageEngine,
                                 sql_engine: SQLEngine):

    obj_text = base_function.bot_text.ordering_text

    await send_base_func_data(callback,
                              base_function,
                              message_engine,
                              sql_engine,
                              obj_text,
                              OrdersTable,
                              inline_base_order_func_menu)

