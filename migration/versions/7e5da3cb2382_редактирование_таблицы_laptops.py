"""редактирование таблицы laptops

Revision ID: 7e5da3cb2382
Revises: 1b27435df02a
Create Date: 2024-03-18 12:58:28.027260

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7e5da3cb2382'
down_revision: Union[str, None] = '1b27435df02a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table("laptops")
    op.create_table("laptops",
                    sa.Column("id", sa.Integer, primary_key=True),
                    sa.Column("cpu", sa.String),
                    sa.Column("videocard", sa.String),
                    sa.Column("ram", sa.String),
                    sa.Column("storage", sa.String),
                    sa.Column("display", sa.String),
                    sa.Column("description", sa.String),
                    sa.Column("product_id", sa.Integer, sa.ForeignKey("all_products.id", ondelete="CASCADE")))

    op.execute("DELETE FROM all_products;")


def downgrade() -> None:
    pass
