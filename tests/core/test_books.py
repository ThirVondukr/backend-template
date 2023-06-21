import uuid

import pytest
from result import Err, Ok
from sqlalchemy.ext.asyncio import AsyncSession

from core.books.dto import BookCreateDTO
from core.books.exceptions import BookAlreadyExistsError
from core.books.services import BookService
from db.models import Book

pytestmark = [pytest.mark.anyio]


async def test_create(
    session: AsyncSession,
    book_service: BookService,
) -> None:
    book = await book_service.create(dto=BookCreateDTO(title=str(uuid.uuid4())))
    assert isinstance(book, Ok)
    assert await session.get(Book, book.value.id)


async def test_create_duplicate_title(
    book: Book,
    book_service: BookService,
) -> None:
    result = await book_service.create(dto=BookCreateDTO(title=book.title))
    assert isinstance(result, Err)
    assert isinstance(result.value, BookAlreadyExistsError)


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
