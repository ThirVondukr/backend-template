from app.core.domain.books.models import Book
from app.core.domain.books.repositories import BookRepository


class BookGetQuery:
    def __init__(self, repository: BookRepository) -> None:
        self._repository = repository

    async def execute(self, book_id: int) -> Book | None:
        return await self._repository.get(id_=book_id)
