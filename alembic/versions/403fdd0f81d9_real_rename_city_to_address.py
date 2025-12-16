"""real rename city to address

Revision ID: 403fdd0f81d9
Revises: 7dbf62d63b1a
Create Date: 2025-12-16 16:58:47.550677

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '403fdd0f81d9'
down_revision: Union[str, Sequence[str], None] = '7dbf62d63b1a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        'user',
        'city',
        new_column_name='address',
        existing_type=sa.String(length=100),
        existing_nullable=True,
    )


def downgrade() -> None:
    op.alter_column(
        'user',
        'address',
        new_column_name='city',
        existing_type=sa.String(length=100),
        existing_nullable=True,
    )