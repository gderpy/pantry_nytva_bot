from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config.db_config import postgres_url


class SQLEngine:

    def __init__(self):
        self.engine = create_async_engine(url=postgres_url, echo=True)
        self.async_session = async_sessionmaker(bind=self.engine, expire_on_commit=False)

