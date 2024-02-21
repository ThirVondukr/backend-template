from collections.abc import AsyncIterator

import dotenv
import httpx
import pytest
from asgi_lifespan import LifespanManager
from fastapi import FastAPI

dotenv.load_dotenv(".env")

pytest_plugins = [
    "anyio",
    "sqlalchemy_pytest.database",
    "tests.plugins.fixture_typecheck",
    "tests.plugins.services",
    "tests.plugins.database",
]


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture(scope="session")
async def fastapi_app() -> AsyncIterator[FastAPI]:
    from app.adapters.api.app import create_app

    app = create_app()
    async with LifespanManager(app=app):
        yield app


@pytest.fixture
async def http_client(fastapi_app: FastAPI) -> AsyncIterator[httpx.AsyncClient]:
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(
            app=fastapi_app,  # type: ignore[arg-type]
        ),
        base_url="http://test",
    ) as client:
        yield client


@pytest.fixture(scope="session")
def worker_id() -> str:
    return "main"
