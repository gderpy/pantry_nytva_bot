from sqlalchemy.orm import Mapped

from ..base import pk_int, fk_product_id, Base


class PowerToolsTable(Base):
    __tablename__ = "power_tools"

    id: Mapped[pk_int]
    description: Mapped[str]
    product_id: Mapped[fk_product_id]