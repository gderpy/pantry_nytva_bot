"""Таблица electronic

Revision ID: 60ee95f1dc94
Revises: e399e808472b
Create Date: 2024-02-25 17:57:10.473930

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '60ee95f1dc94'
down_revision: Union[str, None] = 'e399e808472b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table("electronic",
                sa.Column("id", sa.Integer, primary_key=True),
                 sa.Column("name", sa.String, nullable=False),
                 sa.Column("price", sa.Integer, nullable=False),
                 sa.Column("description", sa.String, nullable=True),
                 sa.Column("category_id", sa.Integer, nullable=True),
                 sa.ForeignKeyConstraint(["category_id"], ["categories.id"]))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("electronic")
    # ### end Alembic commands ###
