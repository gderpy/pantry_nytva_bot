from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey

from .base import Base


class PowerToolsTable(Base):
    __tablename__ = "power_tools"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column()
    description: Mapped[str] = mapped_column()
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    @staticmethod
    def get_column_names():
        return ["name", "price", "description", "category_id"]