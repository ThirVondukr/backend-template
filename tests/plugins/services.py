import uuid

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.domain.books.dto import BookCreateDTO
from app.core.domain.books.models import Book
from app.core.domain.books.repositories import BookRepository
from app.core.domain.books.services import BookService
from lib.db import DBContext


@pytest.fixture
def db_context(session: AsyncSession) -> DBContext:
    return DBContext(session)


@pytest.fixture
def book_repository(session: AsyncSession) -> BookRepository:
    return BookRepository(
        session=session,
    )


@pytest.fixture
def book_service(book_repository: BookRepository, db_context: DBContext) -> BookService:
    return BookService(
        repository=book_repository,
        db_context=db_context,
    )


@pytest.fixture
async def book(book_service: BookService) -> Book:
    book = await book_service.create(dto=BookCreateDTO(title=str(uuid.uuid4())))
    return book.unwrap()
