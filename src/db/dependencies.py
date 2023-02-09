from collections.abc import AsyncIterable

from fastapi.requests import Request
from sqlalchemy.ext.asyncio import AsyncSession

from .engine import async_session_factory


async def get_session(request: Request) -> AsyncIterable[AsyncSession]:
    async with async_session_factory() as session:
        request.state.sqlalchemy_session = session
        yield session
