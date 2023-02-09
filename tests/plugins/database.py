import os

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from alembic import config
from db.engine import async_session_factory


@pytest.fixture(scope="session")
def database_url() -> str:
    return os.environ["DATABASE_TEST_URL"]


@pytest.fixture(scope="session", name="async_sessionmaker")
def async_sessionmaker_() -> async_sessionmaker[AsyncSession]:
    return async_session_factory


@pytest.fixture(scope="session")
def alembic_config() -> config.Config | None:
    return config.Config("alembic.ini")
