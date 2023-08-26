from collections.abc import Sequence
from typing import Protocol

from db import Base


class DBContext(Protocol):
    """
    Constrained interface for sqlalchemy AsyncSession.

    It's meant to be used in services or commands to persist data
    without having to reach out for AsyncSession directly.
    """

    def add(self, model: Base) -> None:
        ...

    async def flush(self, objects: Sequence[Base] | None = ...) -> None:
        ...
