"""Add address_updates table

Revision ID: 20250529212141
Revises: 
Create Date: 2025-05-29 21:21:41.000000

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '20250529212141'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'address_updates',
        sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
        sa.Column('order_id', sa.String(), nullable=False, comment='The ID of the order being updated'),
        sa.Column('platform', sa.String(), nullable=False, comment='Platform where the order was placed'),
        sa.Column('shipping_address', postgresql.JSON(astext_type=sa.Text()), nullable=False, comment='New shipping address details'),
        sa.Column('billing_address', postgresql.JSON(astext_type=sa.Text()), nullable=True, comment='New billing address details (if different from shipping)'),
        sa.Column('status', sa.String(), nullable=False, server_default='pending', comment='Status of the address update'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), onupdate=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_address_updates_order_id'), 'address_updates', ['order_id'], unique=False)

def downgrade():
    op.drop_index(op.f('ix_address_updates_order_id'), table_name='address_updates')
    op.drop_table('address_updates')
