"""Меняем колонку posting_date

Revision ID: 288d9189b162
Revises: fb9f6c8684eb
Create Date: 2024-03-02 22:59:05.595697

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '288d9189b162'
down_revision: Union[str, None] = 'fb9f6c8684eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("orders_table")
    op.drop_table("sells_table")

    op.execute("CREATE TABLE orders_table ("
               "id SERIAL PRIMARY KEY,"
               "name VARCHAR(128),"
               "contact VARCHAR(128),"
               "posting_date TIMESTAMP DEFAULT current_timestamp);")

    op.execute("CREATE TABLE sells_table ("
               "id SERIAL PRIMARY KEY,"
               "name VARCHAR(128),"
               "price INTEGER,"
               "contact VARCHAR(128),"
               "posting_date TIMESTAMP DEFAULT current_timestamp);")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
