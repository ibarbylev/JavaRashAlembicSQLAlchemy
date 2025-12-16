"""change city column type

Revision ID: 1ee2a1d447d3
Revises: 3b3bc4b2d744
Create Date: 2025-12-16 12:36:18.898493

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1ee2a1d447d3'
down_revision: Union[str, Sequence[str], None] = '3b3bc4b2d744'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        'user',
        'city',
        existing_type=sa.String(),
        type_=sa.String(length=100),
        existing_nullable=True
    )


def downgrade() -> None:
    op.alter_column(
        'user',
        'city',
        existing_type=sa.String(length=100),
        type_=sa.String(),
        existing_nullable=True
    )
