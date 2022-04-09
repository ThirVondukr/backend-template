import os
from typing import AsyncIterable

import pytest
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine

from db import Base
from db.base import async_sessionmaker


@pytest.fixture(scope="session")
def engine() -> AsyncEngine:
    return create_async_engine(
        os.environ["DATABASE_TEST_URL"],
        future=True,
        pool_use_lifo=True,
        pool_size=20,
    )


@pytest.fixture(autouse=True)
async def session(engine: AsyncEngine) -> AsyncSession:
    async with engine.connect() as conn:
        transaction = await conn.begin()
        async_sessionmaker.configure(bind=conn)

        async with async_sessionmaker() as session:
            yield session

        if transaction.is_active:
            await transaction.rollback()


@pytest.fixture(scope="session", autouse=True)
async def setup_database(engine: AsyncEngine) -> AsyncIterable[None]:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
