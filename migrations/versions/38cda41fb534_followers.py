"""followers

Revision ID: 38cda41fb534
Revises: 83cc52268ec7
Create Date: 2018-05-14 09:20:09.484050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38cda41fb534'
down_revision = '83cc52268ec7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
