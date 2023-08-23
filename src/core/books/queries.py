from core.books.services import BookService
from db.models import Book


class GetBookQuery:
    def __init__(self, book_service: BookService) -> None:
        self._book_service = book_service

    async def execute(self, book_id: int) -> Book | None:
        return await self._book_service.get_one(book_id=book_id)
