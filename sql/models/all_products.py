from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import CheckConstraint

from .base import Base


class AllProductsTable(Base):
    __tablename__ = "all_products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(nullable=False, info={"check": "price >= 0"})
    category: Mapped[str] = mapped_column(nullable=False)

