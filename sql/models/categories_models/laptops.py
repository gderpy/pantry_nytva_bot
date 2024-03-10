from sqlalchemy.orm import Mapped

from ..base import pk_int, fk_product_id, Base


class LaptopsTable(Base):
    __tablename__ = "laptops"

    id: Mapped[pk_int]
    videocard: Mapped[str]
    ram: Mapped[str]
    storage: Mapped[str]
    display: Mapped[str]
    description: Mapped[str]
    product_id: Mapped[fk_product_id]