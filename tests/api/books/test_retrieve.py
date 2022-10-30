import uuid

import httpx
from fastapi import status

from core.books.dto import BookCreateDto
from core.books.services import BookService


async def test_not_found(
    http_client: httpx.AsyncClient,
) -> None:
    response = await http_client.get("/books/1")
    assert response.status_code == status.HTTP_404_NOT_FOUND


async def test_base_case(
    http_client: httpx.AsyncClient,
    book_service: BookService,
) -> None:
    book = await book_service.create(BookCreateDto(title=str(uuid.uuid4())))

    response = await http_client.get(f"/books/{book.id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "id": book.id,
        "title": book.title,
    }
