import uuid

from result import Err, Ok
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.domain.books.dto import BookCreateDTO
from app.core.domain.books.errors import BookAlreadyExistsError
from app.core.domain.books.models import Book
from app.core.domain.books.repositories import BookRepository
from app.core.domain.books.services import BookService


async def test_create(
    session: AsyncSession,
    book_service: BookService,
) -> None:
    book = await book_service.create(dto=BookCreateDTO(title=str(uuid.uuid4())))
    assert isinstance(book, Ok)
    assert await session.get(Book, book.ok_value.id)


async def test_create_duplicate_title(
    book: Book,
    book_service: BookService,
) -> None:
    result = await book_service.create(dto=BookCreateDTO(title=book.title))
    assert isinstance(result, Err)
    assert isinstance(result.err_value, BookAlreadyExistsError)


async def test_get_one(
    book: Book,
    book_repository: BookRepository,
) -> None:
    book_in_db = await book_repository.get(id_=book.id)
    assert book is book_in_db


async def test_get_one_not_found(
    book_repository: BookRepository,
) -> None:
    assert await book_repository.get(id_=1) is None
