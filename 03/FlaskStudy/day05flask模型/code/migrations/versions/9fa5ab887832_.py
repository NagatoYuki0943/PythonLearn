"""empty message

Revision ID: 9fa5ab887832
Revises: d3a288d690db
Create Date: 2021-12-01 17:01:58.349821

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9fa5ab887832"
down_revision = "d3a288d690db"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "user",
        sa.Column("realname", sa.String(length=20), nullable=True, comment="真实姓名"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "realname")
    # ### end Alembic commands ###
