from aiogram.filters.callback_data import CallbackData


class CatalogCF(CallbackData, prefix="catalog"):
    phones: int = 0
    cosmetic: int = 0
    children_goods: int = 0
    electronic: int = 0
    power_tools: int = 0
    tvs: int = 0
    laptops: int = 0


