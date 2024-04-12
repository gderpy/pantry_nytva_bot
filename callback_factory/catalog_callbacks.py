from enum import Enum

from aiogram.filters.callback_data import CallbackData


class UserType(str, Enum):
    user = "user"
    admin = "admin"


class Paginator(str, Enum):
    next_page = "next_page"
    previous_page = "previous_page"


class CatalogLVL1(CallbackData, prefix="catalog_level_1_choose_category"):
    """Выбор категории товара"""
    user_type: UserType


class CatalogLVL2(CallbackData, prefix="catalog_level_2_electronic_section"):
    """Раздел электроника"""
    user_type: UserType


class ReturnFromProduct(str, Enum):
    product_with_photo = "product_with_photo"
    product_without_photo = "product_without_photo"


class CatalogLVL3(CallbackData, prefix="catalog"):
    """Отображение товара категории"""
    user_type: UserType

    category: str
    page: int = 1
    paginator: Paginator | bool = False

    return_from_product: ReturnFromProduct | bool = False

















