import asyncio

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import select, delete, text, func

from config.db_config import postgres_url
from sql.models import SellsTable, AllProductsTable, Base
from sql.models.categories_models import (PhonesTable, CosmeticsTable, ChildrenGoodsTable,
                                          ElectronicTable, PowerToolsTable, TvTable, LaptopsTable)


class SQLEngine:

    def __init__(self):
        self.engine = create_async_engine(url=postgres_url, echo=True)

        self.async_session: async_sessionmaker[AsyncSession] = (
            async_sessionmaker(bind=self.engine, expire_on_commit=False))


    async def insert_objects(self, model: DeclarativeBase, data: dict):
        async with self.async_session() as session:
            async with session.begin():
                session.add(model(**data))
                await session.commit()

    async def select_objects(self, model: DeclarativeBase):
        async with self.async_session() as session:
            stmt = select(model)
            res = await session.execute(stmt)

            data: dict = {}

            for data in res.scalars():
                print(f"data - {data}")

            await session.commit()

    async def get_category_id_from_categories(self, sheet_name: str):
        """Получить id определенной категории, чтобы установить внешний ключ"""
        async with self.async_session() as session:
            stmt = select(AllProductsTable.id).order_by()
            res = await session.execute(stmt)

            await session.commit()

            for data_category_id in res.scalars():
                return data_category_id

    async def get_last_id(self):
        async with self.async_session() as session:
            stmt = select(AllProductsTable).order_by(AllProductsTable.id.desc()).limit(1)
            res = await session.scalar(stmt)
            await session.commit()
            return res.id

    async def clear_the_tables(self, model: DeclarativeBase):
        async with self.async_session() as session:
            stmt = delete(model)
            await session.execute(stmt)

            await session.commit()

    async def count_products_in_category(self, model: DeclarativeBase):
        async with self.async_session() as session:
            stmt = select(func.count(model.id))
            res = await session.scalar(stmt)
            await session.commit()
            print(f"res: {res}")
            return res

    async def display_a_product_of_a_specific_category(self, category: str):
        async with self.async_session() as session:

            stmt = select(AllProductsTable).where(AllProductsTable.category == category)
            res = await session.execute(stmt)

            await session.commit()

            product_and_price = {}

            def format_price(price):
                return "{:,}".format(price).replace(",", " ")

            for number, data in enumerate(res.scalars(), start=1):
                # product_and_price[number] = f"{data.name} - {format_price(data.price)} руб"
                product_and_price[number] = {
                    "catalog_name": f"{data.name} - {format_price(data.price)} руб",
                    "id": data.id
                }

            return product_and_price

    async def define_product_id(self, product_name: str):
        async with self.async_session() as session:

            stmt = select(AllProductsTable).where(AllProductsTable.name == product_name)
            res = await session.execute(stmt)
            product = res.scalars().first()
            print(product.id)
            await session.commit()
            return product.id















