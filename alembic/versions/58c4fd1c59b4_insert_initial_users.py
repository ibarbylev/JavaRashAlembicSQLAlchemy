"""insert initial users

Revision ID: 58c4fd1c59b4
Revises: ce973c8f81fd
Create Date: 2025-12-16 01:51:35.797755

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '58c4fd1c59b4'
down_revision: Union[str, Sequence[str], None] = 'ce973c8f81fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Вставка 5 пользователей в таблицу user
    op.bulk_insert(
        sa.table(
            'user',
            sa.column('id', sa.Integer),
            sa.column('name', sa.String),
            sa.column('age', sa.Integer),
            sa.column('email', sa.String)
        ),
        [
            {'id': 1, 'name': 'Alice', 'age': 25, 'email': 'alice@example.com'},
            {'id': 2, 'name': 'Bob', 'age': 30, 'email': 'bob@example.com'},
            {'id': 3, 'name': 'Charlie', 'age': 22, 'email': 'charlie@example.com'},
            {'id': 4, 'name': 'Diana', 'age': 28, 'email': 'diana@example.com'},
            {'id': 5, 'name': 'Eve', 'age': 35, 'email': 'eve@example.com'},
        ]
    )

def downgrade() -> None:
    # Удаляем эти записи при откате миграции
    op.execute(
        "DELETE FROM user WHERE id IN (1, 2, 3, 4, 5)"
    )
