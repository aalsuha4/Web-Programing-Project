"""followers

Revision ID: 9468973784ee
Revises: 3d82de54fa62
Create Date: 2018-10-22 21:01:49.366097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9468973784ee'
down_revision = '3d82de54fa62'
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
