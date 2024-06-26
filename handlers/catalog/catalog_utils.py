import logging

from functools import wraps
from aiogram.types import CallbackQuery

from sql.sql_engine import SQLEngine

categories_dict = {
    "phones": "Смартфоны",
    "cosmetic": "Лэтуаль",
    "children_goods": "Детские товары",
    "electronic": "Электроника",
    "power_tools": "Электроинструменты",
    "tvs": "Телевизоры",
    "laptops": "Ноутбуки"
}


def get_products_from_category(func):
    @wraps(func)
    async def wrapped(callback: CallbackQuery, sql_engine: SQLEngine, *args, **kwargs):
        # Достаем название категории из CallbackFactory
        new_instance_callback = CatalogCF.unpack(value=callback.data)
        category = new_instance_callback.category

        # Определяем текущую страницу каталога
        if new_instance_callback.paginator == "next_page":
            new_instance_callback.page += 1
        elif new_instance_callback.paginator == "previous_page":
            new_instance_callback.page -= 1

        current_page = new_instance_callback.page

        # Определяем название категории в таблице
        table_category = categories_dict.get(category)
        # Проводим выборку товаров по категории
        products = await sql_engine.display_a_product_of_a_specific_category(category=table_category)

        return await func(callback=callback,
                          category=category,
                          table_category=table_category,
                          products=products,
                          current_page=current_page,
                          sql_engine=SQLEngine,
                          *args, **kwargs)

    return wrapped


def show_alert_if_products_are_missing(func):
    @wraps(func)
    async def wrapped(*args, **kwargs):

        if "callback" in kwargs and "products" in kwargs:
            callback = kwargs["callback"]
            products = kwargs["products"]

            check = False

            if len(products) == 0:
                return await callback.answer(
                    text="В данной категории товары отсутствуют",
                    show_alert=True
                )
            else:
                check = True
                return await func(*args, **kwargs, check=check)

        else:
            raise KeyError("Ключи: CallbackQuery/products не обнаружены")

    return wrapped


def photo_upload_check(func):
    @wraps(func)
    async def wrapped(*args, **kwargs):

        print("kwargs")
        print(kwargs)
        print()

        if "callback" in kwargs:
            callback = kwargs["callback"]

        photo_check = False

        cf_name = kwargs.get("callback_factory").__class__.__name__
        cf_new_instance = kwargs.get("callback_factory")

        if cf_name in ["CatalogCF", "ProductCF"]:
            photo_check = cf_new_instance.photo

        print()
        print(f"{cf_name}: {photo_check}")

        return await func(*args, **kwargs, photo_check=photo_check)

    return wrapped


