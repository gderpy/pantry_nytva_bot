from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, pk_int


class AllProductsTable(Base):
    __tablename__ = "all_products"

    id: Mapped[pk_int]
    name: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(nullable=False, info={"check": "price >= 0"})
    category: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        return (f"AllProductsTable: "
                f"id: {self.id}, "
                f"name: {self.name}, "
                f"price: {self.price}, "
                f"category: {self.category}")

    def __str__(self):
        return self.__repr__()



    