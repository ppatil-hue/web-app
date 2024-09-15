"""Initial migration

Revision ID: 70f1119c8473
Revises: 
Create Date: 2024-09-15 20:57:19.214243

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '70f1119c8473'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
                    sa.Column('id', sa.Integer(), primary_key=True),
                    sa.Column('username', sa.String(length=64), nullable=False),
                    sa.Column('email', sa.String(length=120), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('username'),
                    sa.UniqueConstraint('email')
                    )

    op.create_table(
        'posts',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id')),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'])
        )



def downgrade() -> None:
    op.drop_table('posts')
    op.drop_table('users')
