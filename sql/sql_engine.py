from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import select

from config.db_config import postgres_url
from sql.models import SellTable


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












