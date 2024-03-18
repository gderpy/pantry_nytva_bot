from enum import Enum

from aiogram.filters.callback_data import CallbackData


class Paginator(str, Enum):
    next_page = "next_page"
    previous_page = "previous_page"


class CatalogCF(CallbackData, prefix="catalog"):
    category: str | int = 0

    product_number: int = 0
    paginator: Paginator | bool = False
    page: int = 1


class ProductCF(CallbackData, prefix="product"):
    category: str | int = 0
    product_number: int = 0
    from_page: int = 1
    product_id: int






