import contextlib
from collections.abc import AsyncIterator

from fastapi.requests import Request
from sqlalchemy.ext.asyncio import AsyncSession

from .engine import async_session_factory


async def get_session(request: Request) -> AsyncIterator[AsyncSession]:
    async with async_session_factory() as session:
        request.state.sqlalchemy_session = session
        yield session


@contextlib.asynccontextmanager
async def create_session() -> AsyncIterator[AsyncSession]:
    async with async_session_factory() as session:
        yield session
