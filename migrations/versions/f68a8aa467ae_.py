"""empty message

Revision ID: f68a8aa467ae
Revises: 2b17daf9e4c0
Create Date: 2021-03-25 02:10:15.024163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f68a8aa467ae'
down_revision = '2b17daf9e4c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'likes', ['userId', 'postId', 'commentId'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'likes', type_='unique')
    # ### end Alembic commands ###
