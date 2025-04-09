from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.domain.books.models import Book


async def test_books_db(session: AsyncSession) -> None:
    book_count = 10
    session.add_all([Book(title=f"{i}") for i in range(book_count)])
    await session.flush()

    books = (await session.scalars(select(Book))).all()
    assert len(books) == book_count
