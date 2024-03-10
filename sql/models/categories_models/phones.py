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


print(PhonesTable.collect_column_names())


