"""empty message

Revision ID: c915ccf44561
Revises: 02a1c5275dd3
Create Date: 2020-08-07 15:04:21.120674

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c915ccf44561'
down_revision = '02a1c5275dd3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    op.add_column('chapter', sa.Column('chapter_all', sa.String(length=50), nullable=True))
    op.add_column('chapter', sa.Column('chapter_main', sa.String(length=50), nullable=True))
    op.add_column('chapter', sa.Column('html_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'chapter', 'html', ['html_id'], ['id'])
    op.drop_column('chapter', 'chapter_html_after')
    op.drop_column('chapter', 'chapter_name_before')
    op.drop_column('chapter', 'chapter_name_after')
    op.drop_column('chapter', 'chapter_html_before')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chapter', sa.Column('chapter_html_before', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('chapter', sa.Column('chapter_name_after', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('chapter', sa.Column('chapter_name_before', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('chapter', sa.Column('chapter_html_after', mysql.VARCHAR(length=50), nullable=True))
    op.drop_constraint(None, 'chapter', type_='foreignkey')
    op.drop_column('chapter', 'html_id')
    op.drop_column('chapter', 'chapter_main')
    op.drop_column('chapter', 'chapter_all')
    op.create_table('book',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('content_before', mysql.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    # ### end Alembic commands ###
