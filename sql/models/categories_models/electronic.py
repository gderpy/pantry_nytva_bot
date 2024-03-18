from sqlalchemy.orm import Mapped

from ..base import pk_int, fk_product_id, Base


class ElectronicTable(Base):
    __tablename__ = "electronic"

    id: Mapped[pk_int]
    description: Mapped[str]
    product_id: Mapped[fk_product_id]

    def __repr__(self):
        return (f"ElectronicTable: "
                f"id: {self.id}, "
                f"description: {self.description}, "
                f"product_id: {self.product_id}")

    def __str__(self):
        return self.__repr__()

