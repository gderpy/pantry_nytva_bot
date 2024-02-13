from aiogram import F, Router
from aiogram.types import CallbackQuery


router = Router()

@router.callback_query(F.data == "order_a_product")
async def handle_ordering_product(callback: CallbackQuery):
    pass