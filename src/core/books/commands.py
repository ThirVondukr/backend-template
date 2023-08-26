from result import Result

from db.models import Book

from .dto import BookCreateDTO
from .errors import BookAlreadyExistsError
from .services import BookService


class BookCreateCommand:
    def __init__(
        self,
        book_service: BookService,
    ) -> None:
        self._book_service = book_service

    async def execute(self, dto: BookCreateDTO) -> Result[Book, BookAlreadyExistsError]:
        return await self._book_service.create(dto=dto)
