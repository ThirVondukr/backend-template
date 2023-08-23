import contextlib
from collections.abc import AsyncIterator

import aioinject
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from core.types import Providers

from ._engine import async_session_factory, engine


@contextlib.asynccontextmanager
async def create_engine() -> AsyncIterator[AsyncEngine]:
    yield engine
    await engine.dispose()


@contextlib.asynccontextmanager
async def create_session(_: AsyncEngine) -> AsyncIterator[AsyncSession]:
    async with async_session_factory.begin() as session:
        yield session


providers: Providers = [
    aioinject.Singleton(create_engine),
    aioinject.Callable(create_session),
]
