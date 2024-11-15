"""Removing pk column in users_programs table

Revision ID: 3a24218c3d1d
Revises: 2a2175c759ff
Create Date: 2024-11-08 16:03:12.404373

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '3a24218c3d1d'
down_revision = '2a2175c759ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users_programs', schema=None) as batch_op:
        batch_op.drop_column('pk')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users_programs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pk', sa.INTEGER(), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
