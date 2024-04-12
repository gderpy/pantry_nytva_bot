from sqlalchemy.orm import Mapped

from sql.models.base import Base, fk_product_id


class Photos(Base):
    __tablename__ = "photos"

    file_id: Mapped[str]
    product_id: Mapped[fk_product_id]


