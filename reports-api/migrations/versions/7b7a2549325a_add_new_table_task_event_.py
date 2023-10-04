"""add new table task event responsibilities

Revision ID: 7b7a2549325a
Revises: aa8b9c1aff7f
Create Date: 2023-09-28 18:37:14.866034

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7b7a2549325a'
down_revision = 'aa8b9c1aff7f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task_event_responsibilities',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('task_event_id', sa.Integer(), nullable=False),
    sa.Column('responsibility_id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=True),
    sa.Column('updated_by', sa.String(length=255), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('is_active', sa.Boolean(), server_default='t', nullable=False),
    sa.Column('is_deleted', sa.Boolean(), server_default='f', nullable=False),
    sa.ForeignKeyConstraint(['responsibility_id'], ['responsibilities.id'], ),
    sa.ForeignKeyConstraint(['task_event_id'], ['task_events.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sqlite_autoincrement=True
    )
    op.create_table('task_event_responsibilities_history',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('task_event_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('responsibility_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('created_by', sa.String(length=255), autoincrement=False, nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), autoincrement=False, nullable=True),
    sa.Column('updated_by', sa.String(length=255), autoincrement=False, nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.Boolean(), autoincrement=False, nullable=False),
    sa.Column('is_deleted', sa.Boolean(), autoincrement=False, nullable=False),
    sa.Column('pk', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('during', postgresql.TSTZRANGE(), nullable=True),
    sa.ForeignKeyConstraint(['responsibility_id'], ['responsibilities.id'], ),
    sa.ForeignKeyConstraint(['task_event_id'], ['task_events.id'], ),
    sa.PrimaryKeyConstraint('id', 'pk'),
    sqlite_autoincrement=True
    )
    op.drop_constraint('task_events_responsibility_id_fkey', 'task_events', type_='foreignkey')
    op.drop_column('task_events', 'responsibility_id')
    op.drop_constraint('task_events_history_responsibility_id_fkey', 'task_events_history', type_='foreignkey')
    op.drop_column('task_events_history', 'responsibility_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task_events_history', sa.Column('responsibility_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('task_events_history_responsibility_id_fkey', 'task_events_history', 'responsibilities', ['responsibility_id'], ['id'])
    op.add_column('task_events', sa.Column('responsibility_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('task_events_responsibility_id_fkey', 'task_events', 'responsibilities', ['responsibility_id'], ['id'])
    op.drop_table('task_event_responsibilities_history')
    op.drop_table('task_event_responsibilities')
    # ### end Alembic commands ###
