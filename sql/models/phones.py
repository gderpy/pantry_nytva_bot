from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey

from .base import Base


class PhoneTable(Base):
    __tablename__ = "phones"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column()
    description: Mapped[str] = mapped_column()
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

