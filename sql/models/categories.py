from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class CategoriesTable(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

