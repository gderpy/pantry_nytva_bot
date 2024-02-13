from aiogram.fsm.state import State, StatesGroup


class FSMSellingProduct(StatesGroup):
    name = State()
    price = State()
    product_link = State()
    product_photo = State()
    phone_number = State()

