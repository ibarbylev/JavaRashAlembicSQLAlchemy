"""manual rename user table to account

Revision ID: 637a667a152c
Revises: 6930bb8b7e58
Create Date: 2025-12-18 18:24:38.822418

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '637a667a152c'
down_revision: Union[str, Sequence[str], None] = '6930bb8b7e58'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table(
        'user',
        'account'
    )


def downgrade() -> None:
    op.rename_table(
        'account',
        'user'
    )
