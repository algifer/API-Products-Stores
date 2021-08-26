"""empty message

Revision ID: 62d623db3d15
Revises: 
Create Date: 2021-08-25 23:37:53.833738

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '62d623db3d15'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('idProduct', sa.Integer(), nullable=False),
    sa.Column('sku', sa.String(), nullable=False),
    sa.Column('information', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('idProduct'),
    sa.UniqueConstraint('sku')
    )
    op.create_table('stores',
    sa.Column('idStore', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('information', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('idStore'),
    sa.UniqueConstraint('name')
    )
    op.create_table('storeProducts',
    sa.Column('idStoreProducts', sa.Integer(), nullable=False),
    sa.Column('id_store', sa.Integer(), nullable=True),
    sa.Column('id_product', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_product'], ['products.idProduct'], ),
    sa.ForeignKeyConstraint(['id_store'], ['stores.idStore'], ),
    sa.PrimaryKeyConstraint('idStoreProducts')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('storeProducts')
    op.drop_table('stores')
    op.drop_table('products')
    # ### end Alembic commands ###