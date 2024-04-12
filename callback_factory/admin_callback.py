from enum import Enum
from aiogram.filters.callback_data import CallbackData


class AdminCF(CallbackData, prefix="admin"):
    excel_parser: int = 0
    catalog_editor: int = 0
    excel_parser_download: int = 0
    excel_parser_upload: int = 0
    excel_parser_cancel_upload: int = 0


class Level(str, Enum):
    back_admin_menu = "admin_menu"
    choose_category = "category"
    choose_product = "product"
    electronic_section = "electronic"


class ProductPhotoCF(CallbackData, prefix="photo"):

    product_id: int = 0

    page: int = 0

    category: str | int = 0







