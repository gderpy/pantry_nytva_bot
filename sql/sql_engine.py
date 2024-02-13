from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from config.db_config import postgres_url


class SQLEngine:
    def __init__(self):
        self.engine = create_async_engine(url=postgres_url, echo=True)
        self.async_session = async_sessionmaker(bind=self.engine, expire_on_commit=False)

    async def insert_objects(self, model: DeclarativeBase, data: dict):
        async with self.async_session() as session:
            async with session.begin():
                session.add(model(**data))
                await session.commit()