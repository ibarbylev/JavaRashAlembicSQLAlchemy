"""add city column to user

Revision ID: 3b3bc4b2d744
Revises: 58c4fd1c59b4
Create Date: 2025-12-16 02:46:04.262640

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3b3bc4b2d744'
down_revision: Union[str, Sequence[str], None] = '58c4fd1c59b4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Добавляем новую колонку city
    op.add_column('user', sa.Column('city', sa.String(), nullable=True))

    # 2. Заполняем данные для существующих пользователей
    op.execute("""
        UPDATE "user"
        SET city = CASE id
            WHEN 1 THEN 'New York'
            WHEN 2 THEN 'Los Angeles'
            WHEN 3 THEN 'Chicago'
            WHEN 4 THEN 'Houston'
            WHEN 5 THEN 'Miami'
        END
    """)

def downgrade() -> None:
    # Удаляем колонку city при откате миграции
    op.drop_column('user', 'city')
