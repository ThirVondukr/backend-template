import uuid

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from core.books.dto import BookCreateDTO
from core.books.services import BookService
from db.models import Book


@pytest.fixture
def book_service(session: AsyncSession) -> BookService:
    return BookService(
        session=session,
    )


@pytest.fixture
async def book(book_service: BookService) -> Book:
    book = await book_service.create(dto=BookCreateDTO(title=str(uuid.uuid4())))
    return book.unwrap()
