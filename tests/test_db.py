from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Book


async def test_books_db(session: AsyncSession) -> None:
    session.add_all([Book(title=f"{i}") for i in range(10)])
    await session.flush()

    books = (await session.scalars(select(Book))).all()
    assert len(books) == 10
