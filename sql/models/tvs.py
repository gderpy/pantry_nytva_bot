from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey

from .base import Base


class TvTable(Base):
    __tablename__ = "tvs"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column()
    display: Mapped[str] = mapped_column()
    qled: Mapped[str] = mapped_column()
    smart_tv: Mapped[str] = mapped_column()
    hdr: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    @staticmethod
    def get_column_names():
        return ["name", "price", "display", "qled", "smart_tv", "hdr", "description", "category_id"]