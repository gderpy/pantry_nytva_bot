import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DateTime
from datetime import datetime, timezone


class Base(DeclarativeBase):
    pass


class OrderTable(Base):
    __tablename__ = "order_table"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()
    contact: Mapped[str] = mapped_column()
    posting_date = mapped_column(DateTime(), default=datetime.now, nullable=False)

    def as_list(self):
        return [self.name, self.contact, self.posting_date]

    def __repr__(self):
        return (f"OrderTable("
                f"id: {self.id}, "
                f"name: {self.name}, "
                f"contact: {self.contact}, "
                f"posting_date: {self.posting_date}")


class SellTable(Base):
    __tablename__ = "sell_table"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column()
    contact: Mapped[str] = mapped_column()
    posting_date = mapped_column(DateTime(), default=datetime.now, nullable=False)

    def as_list(self):
        return [self.name, self.price, self.contact, self.posting_date]

    def __repr__(self):
        return (f"SellTable("
                f"id: {self.id}, "
                f"name: {self.name}, "
                f"price: {self.price}, "
                f"contact: {self.contact}, "
                f"posting_date: {self.posting_date}")















