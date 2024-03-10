from sqlalchemy.orm import Mapped

from .base import Base, pk_int, posting_date


class OrdersTable(Base):
    __tablename__ = "orders_table"

    id: Mapped[pk_int]
    name: Mapped[str]
    contact: Mapped[str]
    posting_date: Mapped[posting_date]

    def as_list(self):
        return [self.name, self.contact, self.posting_date]

    def __repr__(self):
        return (f"OrderTable("
                f"id: {self.id}, "
                f"name: {self.name}, "
                f"contact: {self.contact}, "
                f"posting_date: {self.posting_date}")


class SellsTable(Base):
    __tablename__ = "sells_table"
    id: Mapped[pk_int]
    name: Mapped[str]
    price: Mapped[int]
    contact: Mapped[str]
    posting_date: Mapped[posting_date]

    def as_list(self):
        return [self.name, self.price, self.contact, self.posting_date]

    def __repr__(self):
        return (f"SellTable("
                f"id: {self.id}, "
                f"name: {self.name}, "
                f"price: {self.price}, "
                f"contact: {self.contact}, "
                f"posting_date: {self.posting_date}")
