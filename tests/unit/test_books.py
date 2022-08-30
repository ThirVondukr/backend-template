import uuid

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from apps.books.dto import BookCreateDto
from apps.books.exceptions import BookAlreadyExists
from apps.books.services import BookService
from db.models import Book


async def test_create(
    session: AsyncSession,
    book_service: BookService,
) -> None:
    book = await book_service.create(dto=BookCreateDto(title=str(uuid.uuid4())))
    assert await session.get(Book, book.id)


async def test_create_duplicate_title(
    book: Book,
    book_service: BookService,
) -> None:

    with pytest.raises(BookAlreadyExists):
        await book_service.create(dto=BookCreateDto(title=book.title))


async def test_get_one(
    book: Book,
    book_service: BookService,
) -> None:
    book_in_db = await book_service.get_one(book_id=book.id)
    assert book is book_in_db


async def test_get_one_not_found(
    book_service: BookService,
) -> None:
    assert await book_service.get_one(book_id=1) is None
