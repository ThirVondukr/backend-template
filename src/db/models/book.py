from sqlalchemy import Column, Integer, String

from db import Base


class Book(Base):
    __tablename__ = "book"

    id: int = Column(Integer, primary_key=True)
    title: str = Column(String(255), nullable=False, unique=True)
