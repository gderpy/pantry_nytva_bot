from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class OrderTable(Base):
    __tablename__ = "order_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    contact: Mapped[str] = mapped_column()


class SellTable(Base):
    __tablename__ = "sell_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column()
    contact: Mapped[str] = mapped_column()














