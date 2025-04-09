from collections.abc import Sequence
from typing import TypeVar

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

T = TypeVar("T", bound=DeclarativeBase)


class DBContext:
    """
    Constrained interface for sqlalchemy AsyncSession.

    It's meant to be used in services or commands to persist data
    without having to reach out for AsyncSession directly.
    """

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    def add(self, model: T) -> None:
        return self._session.add(model)

    def add_all(self, models: Sequence[T]) -> None:
        return self._session.add_all(models)  # pragma: no cover

    async def flush(self, objects: Sequence[T] | None = None) -> None:
        return await self._session.flush(objects)
