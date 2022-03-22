from typing import AsyncIterable

from sqlalchemy.ext.asyncio import AsyncSession

from .base import async_sessionmaker


async def get_session() -> AsyncIterable[AsyncSession]:
    async with async_sessionmaker() as session:
        yield session
