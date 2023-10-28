from collections.abc import Sequence
from typing import Protocol, TypeVar

from sqlalchemy.orm import DeclarativeBase

T = TypeVar("T", bound=DeclarativeBase)


class DBContext(Protocol):
    """
    Constrained interface for sqlalchemy AsyncSession.

    It's meant to be used in services or commands to persist data
    without having to reach out for AsyncSession directly.
    """

    def add(self, model: T) -> None:
        ...

    async def flush(self, objects: Sequence[T] | None = ...) -> None:
        ...
