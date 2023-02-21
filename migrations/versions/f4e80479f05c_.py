"""empty message

Revision ID: f4e80479f05c
Revises: 0499c023d405
Create Date: 2023-02-20 21:33:58.849717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4e80479f05c'
down_revision = '0499c023d405'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('diagnostics', schema=None) as batch_op:
        batch_op.add_column(sa.Column('comments', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('diagnostics', schema=None) as batch_op:
        batch_op.drop_column('comments')

    # ### end Alembic commands ###