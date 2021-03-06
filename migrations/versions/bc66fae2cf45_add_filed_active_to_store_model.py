"""add filed active to Store model

Revision ID: bc66fae2cf45
Revises: 69ca3ab75922
Create Date: 2020-12-05 09:48:22.299198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc66fae2cf45'
down_revision = '69ca3ab75922'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('store', sa.Column('active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('store', 'active')
    # ### end Alembic commands ###
