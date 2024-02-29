from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import select

from sql.sql_engine import SQLEngine
from sql.models.categories import CategoriesTable


class CatalogDisplay:
    def __init__(self):
        self.sql_engine: SQLEngine = SQLEngine()

    async def display_product_list(self, category: str):
        pass