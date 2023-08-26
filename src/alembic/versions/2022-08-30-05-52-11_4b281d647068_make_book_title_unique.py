"""
Make book title unique

Revision ID: 4b281d647068
Revises: 7722a16c2bac
Create Date: 2022-08-30 05:52:11.173003

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "4b281d647068"
down_revision = "7722a16c2bac"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_unique_constraint(op.f("uq_book_title"), "book", ["title"])


def downgrade() -> None:
    op.drop_constraint(op.f("uq_book_title"), "book", type_="unique")
