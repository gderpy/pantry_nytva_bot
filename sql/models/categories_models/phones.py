from sqlalchemy.orm import Mapped

from sql.models import Base, fk_product_id


class PhonesTable(Base):
    __tablename__ = "phones"

    cpu: Mapped[str]
    ram: Mapped[str]
    storage: Mapped[str]
    display: Mapped[str]
    battery: Mapped[str]
    sim: Mapped[str]
    camera: Mapped[str]
    description: Mapped[str]
    product_id: Mapped[fk_product_id]

    def __str__(self):
        return (f"PhonesTable: "
                f"cpu: {self.cpu}, "
                f"ram: {self.ram}, "
                f"storage: {self.storage}, "
                f"display: {self.display}, "
                f"battery: {self.battery}, "
                f"sim: {self.sim}, "
                f"camera: {self.camera}, "
                f"description: {self.description}")

    def __repr__(self):
        return self.__str__()















