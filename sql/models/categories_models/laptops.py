from sqlalchemy.orm import Mapped

from ..base import pk_int, fk_product_id, Base


class LaptopsTable(Base):
    __tablename__ = "laptops"

    cpu: Mapped[str]
    videocard: Mapped[str]
    ram: Mapped[str]
    storage: Mapped[str]
    display: Mapped[str]
    description: Mapped[str]
    product_id: Mapped[fk_product_id]

    def __repr__(self):
        return (f"LaptopsTable: "
                f"id: {self.id}, "
                f"cpu: {self.cpu}, "
                f"videocard: {self.videocard}, "
                f"ram: {self.ram}, "
                f"storage: {self.storage}, "
                f"display: {self.display}, "
                f"description: {self.description}, "
                f"product_id: {self.product_id}")

    def __str__(self):
        return self.__repr__()