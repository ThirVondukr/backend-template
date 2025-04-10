from __future__ import annotations

import contextlib
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING

import aioinject
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.settings import DatabaseSettings
from lib.db import DBContext

if TYPE_CHECKING:
    from lib.types import Providers


@contextlib.asynccontextmanager
async def make_async_engine(settings: DatabaseSettings) -> AsyncIterator[AsyncEngine]:
    engine = create_async_engine(
        settings.url,
        pool_size=20,
        pool_pre_ping=True,
        pool_use_lifo=True,
        echo=settings.echo,
    )
    try:
        yield engine
    finally:
        await engine.dispose()


async def make_async_sessionmaker(
    engine: AsyncEngine,
) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(bind=engine)


@contextlib.asynccontextmanager
async def create_session(
    sessionmaker: async_sessionmaker[AsyncSession],
) -> AsyncIterator[AsyncSession]:
    async with sessionmaker.begin() as session:
        yield session


async def db_context(session: AsyncSession) -> DBContext:
    return DBContext(session)


providers: Providers = [
    aioinject.Singleton(make_async_engine),
    aioinject.Singleton(make_async_sessionmaker),
    aioinject.Scoped(create_session),
    aioinject.Scoped(db_context),
]
