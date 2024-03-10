from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, pk_int


class AllProductsTable(Base):
    __tablename__ = "all_products"

    id: Mapped[pk_int]
    name: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(nullable=False, info={"check": "price >= 0"})
    category: Mapped[str] = mapped_column(nullable=False)

    