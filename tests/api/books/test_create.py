import uuid

import httpx
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession

from core.books.services import BookService
from db.models import Book


async def test_base_case(
    http_client: httpx.AsyncClient,
    session: AsyncSession,
    book_service: BookService,
) -> None:
    title = str(uuid.uuid4())
    response = await http_client.post(url="/books", json={"title": title})
    assert response.status_code == status.HTTP_201_CREATED
    response_json = response.json()
    assert response_json["title"] == title
    assert await session.get(Book, response_json["id"])


async def test_duplicate_title(
    http_client: httpx.AsyncClient,
    session: AsyncSession,
    book: Book,
) -> None:
    response = await http_client.post(url="/books", json={"title": book.title})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
