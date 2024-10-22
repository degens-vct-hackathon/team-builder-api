"""create_game_round_table

Revision ID: f06d255fd410
Revises: 
Create Date: 2024-10-22 02:21:01.269489

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f06d255fd410'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'game_rounds',
        sa.Column('id', sa.String, primary_key=True),
        sa.Column('map', sa.String, nullable=False),
        sa.Column('game_id', sa.String, nullable=False),
        sa.Column('round_number', sa.Integer, nullable=False),
        sa.Column('tournament', sa.String, nullable=False),
        sa.Column('winner', sa.Integer, nullable=False),
        sa.Column('offense_wins', sa.Integer, nullable=False),
        sa.Column('defense_wins', sa.Integer, nullable=False)
    )

def downgrade():
    op.drop_table('game_rounds')