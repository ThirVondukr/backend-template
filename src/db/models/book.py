from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped

from db import Base


class Book(Base):
    __tablename__ = "book"

    id: Mapped[int] = Column(Integer, primary_key=True)
    title: Mapped[str] = Column(String(255), nullable=False)
