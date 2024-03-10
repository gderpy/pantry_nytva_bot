from typing import Annotated
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, declared_attr
from sqlalchemy import ForeignKey, text
from datetime import datetime


pk_int = Annotated[int, mapped_column(primary_key=True)]
fk_product_id = Annotated[int, mapped_column(ForeignKey(column="all_products.id",
                                                        ondelete="CASCADE"))]


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __table_args__(cls) -> dict:
        return {'extend_existing': True}

    @classmethod
    def collect_column_names(cls):
        columns = [attr for attr, value in cls.__dict__.items() if isinstance(value, Mapped) and attr != "id"]
        return columns

    id: Mapped[pk_int]


posting_date = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]


# created_at: Mapped[datetime.datetime] =
# mapped_column(server_default=text("TIMEZONE('utc', now())"))

# updated_at: Mapped[datetime.datetime] =
# mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.utcnow)



















