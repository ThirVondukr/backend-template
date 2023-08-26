"""
Initial migration

Revision ID: 7722a16c2bac
Revises:
Create Date: 2022-06-28 17:42:57.806286

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "7722a16c2bac"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "book",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("book")
