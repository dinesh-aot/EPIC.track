"""create linked_work table

Revision ID: b724615d3fdf
Revises: c64aaa268112
Create Date: 2024-05-05 10:45:18.936600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b724615d3fdf'
down_revision = 'c64aaa268112'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('LinkedWorks',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('source_work_id', sa.Integer(), nullable=False),
    sa.Column('linked_work_id', sa.Integer(), nullable=False),
    sa.Column('source_event_id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=True),
    sa.Column('updated_by', sa.String(length=255), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('is_active', sa.Boolean(), server_default='t', nullable=False),
    sa.Column('is_deleted', sa.Boolean(), server_default='f', nullable=False),
    sa.ForeignKeyConstraint(['linked_work_id'], ['works.id'], ),
    sa.ForeignKeyConstraint(['source_event_id'], ['events.id'], ),
    sa.ForeignKeyConstraint(['source_work_id'], ['works.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('LinkedWorks')
    # ### end Alembic commands ###
