from result import Err, Ok, Result

from db import DBContext
from db.models import Book

from .dto import BookCreateDTO
from .errors import BookAlreadyExistsError
from .repositories import BookRepository


class BookService:
    def __init__(
        self,
        repository: BookRepository,
        db_context: DBContext,
    ) -> None:
        self._repository = repository
        self._db_context = db_context

    async def create(
        self,
        dto: BookCreateDTO,
    ) -> Result[Book, BookAlreadyExistsError]:
        if await self._repository.get(title=dto.title) is not None:
            return Err(BookAlreadyExistsError())

        book = Book(
            title=dto.title,
        )
        self._db_context.add(book)
        await self._db_context.flush()
        return Ok(book)
