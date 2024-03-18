import logging

from functools import wraps
from aiogram.types import CallbackQuery

from callback_factory.catalog_callbacks import ProductCF
from handlers.catalog.catalog_utils import categories_dict
from sql.sql_engine import SQLEngine


def get_product_information(func):
    @wraps(func)
    async def wrapped(callback: CallbackQuery, sql_engine: SQLEngine, *args, **kwargs):
        new_instance_callback = ProductCF.unpack(value=callback.data)
        category = new_instance_callback.category
        product_number = new_instance_callback.product_number

        table_category = categories_dict.get(category)
        products = await sql_engine.display_a_product_of_a_specific_category(category=table_category)
        name = products.get(product_number)
        id_product = sql_engine.define_product_id(product_name=name)
        return await func(products=products, *args, **kwargs)

