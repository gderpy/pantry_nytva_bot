import datetime

from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State

from handlers.base_functions.base_functions_engine import BaseFunctionsEngine
from message_engine import MessageEngine
from keyboards.main_keyboard import (inline_base_sell_func_menu, inline_base_sell_func_menu_end,
                                     inline_base_order_func_menu_end)
from sql.sql_engine import SQLEngine
from sql.models import SellsTable, OrdersTable


def choose_inline_keyboard(sell: bool, order: bool):
    if sell:
        return inline_base_sell_func_menu_end
    elif order:
        return inline_base_order_func_menu_end


def define_type_update(update: Message | CallbackQuery,
                       message_engine: MessageEngine):

    message_engine.event = update


async def handle_fsm_sell_and_offer_product(message: Message,
                                            state: FSMContext,
                                            base_function: BaseFunctionsEngine,
                                            message_engine: MessageEngine,
                                            obj_text: str,
                                            next_state: State | None,
                                            keyboard: InlineKeyboardMarkup):

    text = base_function.basic_template(obj_text=obj_text)

    await message.delete()
    await message_engine.edit_message(text=text, keyboard=keyboard)

    if next_state:
        await state.set_state(next_state)


async def send_base_func_data(callback: CallbackQuery,
                              base_function: BaseFunctionsEngine,
                              message_engine: MessageEngine,
                              sql_engine: SQLEngine,
                              obj_text: object,
                              model: SellsTable | OrdersTable,
                              keyboard: InlineKeyboardMarkup):

    message_engine.event = callback
    text = base_function.basic_template(obj_text=obj_text)

    print(base_function.name, base_function.price, base_function.contact)

    if model == OrdersTable:
        data = {"name": base_function.name, "contact": base_function.contact}
    else:
        data = {"name": base_function.name, "price": int(base_function.price),
                "contact": base_function.contact}

        print(f"data - {data}")

    await sql_engine.insert_objects(model=model, data=data)
    await message_engine.edit_message(text=text, keyboard=keyboard)
    await callback.answer()


def correct_price(text_price: str):

    only_number = "".join([l for l in text_price if l.isdigit()])

    if only_number.isdigit():
        return only_number
    else:
        return "Неверный формат стоимости. Отправьте повторно"
