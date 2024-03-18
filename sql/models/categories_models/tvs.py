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

    def __repr__(self):
        return (f"TvTable: "
                f"id: {self.id}, "
                f"display: {self.display}, "
                f"qled: {self.qled}, "
                f"smart_tv: {self.smart_tv}, "
                f"hdr: {self.hdr}, "
                f"description: {self.description}, "
                f"product_id: {self.product_id}")

    def __str__(self):
        return self.__repr__()