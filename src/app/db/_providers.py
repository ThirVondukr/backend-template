from __future__ import annotations

import contextlib
from collections.abc import AsyncIterator

import aioinject
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from lib.db import DBContext
from lib.types import Providers

from ._engine import async_session_factory, engine


@contextlib.asynccontextmanager
async def create_engine() -> AsyncIterator[AsyncEngine]:
    yield engine
    await engine.dispose()


@contextlib.asynccontextmanager
async def create_session(_: AsyncEngine) -> AsyncIterator[AsyncSession]:
    async with async_session_factory.begin() as session:
        yield session


async def db_context(session: AsyncSession) -> DBContext:
    return session


providers: Providers = [
    aioinject.Singleton(create_engine),
    aioinject.Callable(create_session),
    aioinject.Callable(db_context),
]
