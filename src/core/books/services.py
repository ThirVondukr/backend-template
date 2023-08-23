from result import Err, Ok, Result
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Book

from .dto import BookCreateDTO
from .exceptions import BookAlreadyExistsError


class BookService:
    def __init__(
        self,
        session: AsyncSession,
    ) -> None:
        self._session = session

    async def get_one(self, book_id: int) -> Book | None:
        return await self._session.get(Book, book_id)

    async def create(self, dto: BookCreateDTO) -> Result[Book, BookAlreadyExistsError]:
        if await self._session.scalar(select(Book).where(Book.title == dto.title)):
            return Err(BookAlreadyExistsError())

        book = Book(
            title=dto.title,
        )
        self._session.add(book)
        await self._session.flush()
        return Ok(book)
