import os

import aioinject
import pytest
from alembic import config
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


@pytest.fixture(scope="session")
def database_url() -> str:
    return os.environ["DATABASE_TEST_URL"]


@pytest.fixture(autouse=True)
def _break_sessionmaker(async_sessionmaker: async_sessionmaker[AsyncSession]) -> None:
    async_sessionmaker.configure(bind=None)


@pytest.fixture(scope="session", name="async_sessionmaker")
async def async_sessionmaker_(
    container: aioinject.Container,
) -> async_sessionmaker[AsyncSession]:
    async with container.context() as ctx:
        return await ctx.resolve(async_sessionmaker[AsyncSession])


@pytest.fixture(scope="session")
def alembic_config() -> config.Config | None:
    return config.Config("alembic.ini")
