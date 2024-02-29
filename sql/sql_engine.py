from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import select, delete

from config.db_config import postgres_url
from sql.models import SellTable
from sql.models.categories import CategoriesTable


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
            stmt = select(CategoriesTable.id).where(CategoriesTable.name == sheet_name)
            res = await session.execute(stmt)

            await session.commit()

            for data_category_id in res.scalars():
                return data_category_id

    async def clear_the_tables(self, model: DeclarativeBase):
        async with self.async_session() as session:
            stmt = delete(model)
            await session.execute(stmt)

            await session.commit()


    async def display_a_product_of_a_specific_category(self):
        async with self.async_session() as session:
            stmt = select(CategoriesTable).join()












