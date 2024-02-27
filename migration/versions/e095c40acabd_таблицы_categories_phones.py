"""Таблицы categories, phones

Revision ID: e095c40acabd
Revises: 7b1fcbda3478
Create Date: 2024-02-15 12:39:52.815217

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, ForeignKeyConstraint


# revision identifiers, used by Alembic.
revision: str = 'e095c40acabd'
down_revision: Union[str, None] = '7b1fcbda3478'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.create_table(
        "categories",
        sa.Column("id", Integer(), primary_key=True),
                 sa.Column("name", String(), nullable=True)
    )

    op.create_table(
        "phones",
        sa.Column("id", Integer(), primary_key=True),
                 sa.Column("name", String(), nullable=True),
                 sa.Column("price", Integer(), nullable=True),
                 sa.Column("description", String(), nullable=True),
                 sa.Column("category_id", Integer(), nullable=True),
                 ForeignKeyConstraint(["category_id"], ["categories.id"])
    )



def downgrade() -> None:
    op.drop_table("phones")
    op.drop_table("categories")
