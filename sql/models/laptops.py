from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey

from .base import Base


class LaptopTable(Base):
    __tablename__ = "laptops"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column()
    cpu: Mapped[str] = mapped_column()
    videocard: Mapped[str] = mapped_column()
    ram: Mapped[int] = mapped_column()
    storage: Mapped[int] = mapped_column()
    display: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    @staticmethod
    def get_column_names():
        return ["name", "price", "cpu", "videocard", "ram", "storage", "display", "description",
                "category_id"]