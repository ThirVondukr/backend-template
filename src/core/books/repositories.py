from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Book


class BookRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get(
        self,
        id_: int | None = None,
        title: str | None = None,
    ) -> Book | None:
        stmt = select(Book)

        if id_ is not None:
            stmt = stmt.where(Book.id == id_)
        if title is not None:
            stmt = stmt.where(Book.title == title)

        return (await self._session.scalars(stmt)).one_or_none()
