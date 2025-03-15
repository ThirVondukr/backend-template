import pkgutil
from collections.abc import AsyncIterator
from datetime import datetime
from typing import cast

import dotenv
import httpx
import pytest
from _pytest.fixtures import SubRequest
from asgi_lifespan import LifespanManager
from fastapi import FastAPI

import tests.plugins
from lib.time import utc_now

dotenv.load_dotenv(".env")

pytest_plugins = [
    "anyio",
    "sqlalchemy_pytest.database",
    *(
        mod.name
        for mod in pkgutil.walk_packages(
            tests.plugins.__path__,
            prefix="tests.plugins.",
        )
        if not mod.ispkg
    ),
]


@pytest.fixture(scope="session", autouse=True)
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
            app=fastapi_app,
        ),
        base_url="http://test",
    ) as client:
        yield client


@pytest.fixture(scope="session")
def worker_id() -> str:
    return "main"


@pytest.fixture
def now() -> datetime:
    return utc_now()


@pytest.fixture(params=[0, 1, 10])
def collection_size(request: SubRequest) -> int:
    return cast("int", request.param)
