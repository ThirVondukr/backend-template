from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db._base import Base


class Book(Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), unique=True)
