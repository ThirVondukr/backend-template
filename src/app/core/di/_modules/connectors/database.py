from __future__ import annotations

import contextlib
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING

import aioinject
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from app.connectors.db import async_session_factory, engine
from lib.db import DBContext

if TYPE_CHECKING:
    from lib.types import Providers


@contextlib.asynccontextmanager
async def create_engine() -> AsyncIterator[AsyncEngine]:
    try:
        yield engine
    finally:
        await engine.dispose()


@contextlib.asynccontextmanager
async def create_session(_: AsyncEngine) -> AsyncIterator[AsyncSession]:
    async with async_session_factory.begin() as session:
        yield session


async def db_context(session: AsyncSession) -> DBContext:
    return DBContext(session)


providers: Providers = [
    aioinject.Singleton(create_engine),
    aioinject.Scoped(create_session),
    aioinject.Scoped(db_context),
]
