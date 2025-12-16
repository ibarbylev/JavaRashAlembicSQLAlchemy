"""rename city to address

Revision ID: 7dbf62d63b1a
Revises: 1ee2a1d447d3
Create Date: 2025-12-16 16:10:16.868289

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7dbf62d63b1a'
down_revision: Union[str, Sequence[str], None] = '1ee2a1d447d3'
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
