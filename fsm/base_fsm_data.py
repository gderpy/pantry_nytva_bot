from aiogram.fsm.state import State, StatesGroup


class FSMSellProduct(StatesGroup):
    name = State()
    price = State()
    contact = State()


class FSMOrderProduct(StatesGroup):
    name = State()
    contact = State()




