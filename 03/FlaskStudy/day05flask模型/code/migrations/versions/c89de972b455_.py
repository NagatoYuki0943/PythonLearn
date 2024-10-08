"""empty message

Revision ID: c89de972b455
Revises: 9fa5ab887832
Create Date: 2021-12-01 20:47:47.034074

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "c89de972b455"
down_revision = "9fa5ab887832"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user_info")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user_info",
        sa.Column(
            "id", mysql.INTEGER(display_width=11), autoincrement=True, nullable=False
        ),
        sa.Column(
            "realname",
            mysql.VARCHAR(collation="utf8mb4_general_ci", length=20),
            nullable=True,
        ),
        sa.Column(
            "gender", mysql.TINYINT(display_width=1), autoincrement=False, nullable=True
        ),
        sa.PrimaryKeyConstraint("id"),
        mysql_collate="utf8mb4_general_ci",
        mysql_default_charset="utf8mb4",
        mysql_engine="MyISAM",
    )
    # ### end Alembic commands ###
