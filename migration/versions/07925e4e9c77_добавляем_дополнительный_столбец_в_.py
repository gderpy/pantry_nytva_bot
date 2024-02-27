"""Добавляем дополнительный столбец в категорию phones

Revision ID: 07925e4e9c77
Revises: e095c40acabd
Create Date: 2024-02-16 19:14:41.901892

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '07925e4e9c77'
down_revision: Union[str, None] = 'e095c40acabd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("phones", sa.Column("photo_id", sa.String, nullable=True))


def downgrade() -> None:
    op.drop_column("phones", "photo_id")
