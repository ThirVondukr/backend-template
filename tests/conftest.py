import os
from collections.abc import AsyncIterator

import dotenv
import httpx
import pytest
import sqlalchemy.ext.asyncio
from fastapi import FastAPI

from alembic import config

dotenv.load_dotenv(".env")
pytest_plugins = [
    "anyio",
    "tests.plugins.services",
    "sqlalchemy_pytest.database",
]


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture(scope="session")
def fastapi_app() -> FastAPI:
    from api.app import create_app

    return create_app()


@pytest.fixture
async def http_client(fastapi_app: FastAPI) -> AsyncIterator[httpx.AsyncClient]:
    async with httpx.AsyncClient(
        app=fastapi_app,
        base_url="http://test",
    ) as client:
        yield client


@pytest.fixture(scope="session")
def worker_id() -> str:
    return "main"


@pytest.fixture(scope="session")
def database_url() -> str:
    return os.environ["DATABASE_TEST_URL"]


@pytest.fixture(scope="session")
def async_sessionmaker() -> sqlalchemy.ext.asyncio.async_sessionmaker[
    sqlalchemy.ext.asyncio.AsyncSession
]:
    import db.engine

    return db.engine.async_sessionmaker


@pytest.fixture(scope="session")
def alembic_config() -> config.Config | None:
    return config.Config("alembic.ini")
