from sqlalchemy.orm import Mapped

from ..base import Base, pk_int


class CategoriesTable(Base):
    __tablename__ = "categories"

    id: Mapped[pk_int]
    name: Mapped[str]