"""reverse renaming of columns

Revision ID: 6930bb8b7e58
Revises: 403fdd0f81d9
Create Date: 2025-12-16 17:27:35.844485

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6930bb8b7e58'
down_revision: Union[str, Sequence[str], None] = '403fdd0f81d9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        'user',
        'address',
        new_column_name='city',
        existing_type=sa.String(length=100),
        existing_nullable=True,
    )


def downgrade() -> None:
    op.alter_column(
        'user',
        'city',
        new_column_name='address',
        existing_type=sa.String(length=100),
        existing_nullable=True,
    )