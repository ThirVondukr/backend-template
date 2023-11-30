import uuid
from http import HTTPStatus

import httpx
import pytest

from app.core.domain.books.dto import BookCreateDTO
from app.core.domain.books.services import BookService

pytestmark = [pytest.mark.anyio, pytest.mark.usefixtures("session")]


async def test_not_found(
    http_client: httpx.AsyncClient,
) -> None:
    response = await http_client.get("/books/1")
    assert response.status_code == HTTPStatus.NOT_FOUND


async def test_base_case(
    http_client: httpx.AsyncClient,
    book_service: BookService,
) -> None:
    book = (await book_service.create(BookCreateDTO(title=str(uuid.uuid4())))).unwrap()

    response = await http_client.get(f"/books/{book.id}")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": book.id,
        "title": book.title,
    }
