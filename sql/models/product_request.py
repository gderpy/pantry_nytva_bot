from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class ProductRequest(Base):

    __tablename__ = "product_reqs"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    price: Mapped[Optional[int]] = mapped_column()

    def __str__(self):
        return f"ProductRequest: [id: {self.id}, name: {self.name}, price: {self.price}]"

    def __repr__(self):
        repr(self.__str__())


