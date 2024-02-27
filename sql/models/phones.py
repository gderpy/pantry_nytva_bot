from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey

from .base import Base


class PhoneTable(Base):
    __tablename__ = "phones"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column()
    cpu: Mapped[str] = mapped_column()
    ram: Mapped[int] = mapped_column()
    storage: Mapped[int] = mapped_column()
    display: Mapped[str] = mapped_column()
    battery: Mapped[str] = mapped_column()
    sim: Mapped[int] = mapped_column()
    camera: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    @staticmethod
    def get_column_names():
        return ["name", "price", "cpu", "ram", "storage", "display", "battery", "sim", "camera",
                "description", "category_id"]