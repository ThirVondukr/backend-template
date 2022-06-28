import os
from typing import Iterable

import pytest
import sqlalchemy_utils
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine

from alembic import command, config
from db.base import async_sessionmaker


@pytest.fixture(scope="session")
def database_url_() -> str:
    return os.environ["DATABASE_TEST_URL"]


@pytest.fixture(scope="session")
def database_url(database_url_: str, worker_id: str) -> str:
    return f"{database_url_}-{worker_id}"


@pytest.fixture(scope="session")
def sync_database_url(database_url: str) -> str:
    return database_url.replace("+asyncpg", "")


@pytest.fixture(scope="session")
def create_database(sync_database_url: str) -> Iterable[None]:
    if not sqlalchemy_utils.database_exists(sync_database_url):
        sqlalchemy_utils.create_database(sync_database_url)

    yield
    sqlalchemy_utils.drop_database(sync_database_url)


@pytest.fixture(scope="session")
def alembic_config() -> config.Config:
    return config.Config("alembic.ini")


@pytest.fixture(scope="session")
async def run_migrations(
    create_database: None,
    engine: AsyncEngine,
    alembic_config: config.Config,
    sync_database_url: str,
) -> None:
    def run_upgrade(connection: Connection, cfg: config.Config) -> None:
        cfg.attributes["connection"] = connection
        command.upgrade(cfg, revision="head")

    async with engine.begin() as conn:
        alembic_config.set_main_option("sqlalchemy.url", sync_database_url)
        await conn.run_sync(run_upgrade, alembic_config)
        await conn.commit()


@pytest.fixture(scope="session")
def engine(database_url: str) -> AsyncEngine:
    return create_async_engine(
        database_url,
        future=True,
        pool_use_lifo=True,
        pool_size=20,
    )


@pytest.fixture(autouse=True)
async def session(
    run_migrations: None,
    engine: AsyncEngine,
) -> AsyncSession:
    async with engine.connect() as conn:
        transaction = await conn.begin()
        async_sessionmaker.configure(bind=conn)

        async with async_sessionmaker() as session:
            yield session

        if transaction.is_active:
            await transaction.rollback()
