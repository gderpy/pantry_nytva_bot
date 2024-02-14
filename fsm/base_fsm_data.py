from aiogram.fsm.state import State, StatesGroup


class FSMBaseFunctions(StatesGroup):
    name = State()
    price = State()


class FSMSellProduct(FSMBaseFunctions):
    pass


class FSMOrderProduct(StatesGroup):
    name = State()




