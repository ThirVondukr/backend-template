import uuid

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from apps.books.dto import BookCreateDto
from apps.books.services import BookService
from db.models import Book


@pytest.fixture
def book_service(session: AsyncSession) -> BookService:
    return BookService(
        session=session,
    )


@pytest.fixture
async def book(book_service: BookService) -> Book:
    return await book_service.create(dto=BookCreateDto(title=str(uuid.uuid4())))
