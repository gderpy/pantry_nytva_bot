from sqlalchemy.orm import Mapped

from ..base import pk_int, fk_product_id, Base


class TvTable(Base):
    __tablename__ = "tvs"

    id: Mapped[pk_int]
    display: Mapped[str]
    qled: Mapped[str]
    smart_tv: Mapped[str]
    hdr: Mapped[str]
    description: Mapped[str]
    product_id: Mapped[fk_product_id]