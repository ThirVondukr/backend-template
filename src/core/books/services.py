from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.dependencies import get_session
from db.models import Book

from .dto import BookCreateDto
from .exceptions import BookAlreadyExistsError


class BookService:
    def __init__(
        self,
        session: AsyncSession = Depends(get_session),
    ) -> None:
        self._session = session

    async def get_one(self, book_id: int) -> Book | None:
        book: Book | None = await self._session.get(Book, book_id)
        return book

    async def create(self, dto: BookCreateDto) -> Book:
        if await self._session.scalar(select(Book).where(Book.title == dto.title)):
            raise BookAlreadyExistsError

        book = Book(**dto.dict())
        self._session.add(book)
        await self._session.flush()
        await self._session.refresh(book)
        return book
