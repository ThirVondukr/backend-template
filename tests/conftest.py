import asyncio
from asyncio import AbstractEventLoop
from typing import AsyncIterable, Iterable

import dotenv
import httpx
import pytest
from fastapi import FastAPI

dotenv.load_dotenv(".env")

pytest_plugins = [
    "conftest_db",
    "conftest_services",
]


@pytest.fixture(scope="session")
def fastapi_app() -> FastAPI:
    from api.app import create_app

    return create_app()


@pytest.fixture(scope="session")
async def http_client(fastapi_app: FastAPI) -> AsyncIterable[httpx.AsyncClient]:
    async with httpx.AsyncClient(
        app=fastapi_app,
        base_url="http://test",
    ) as client:
        yield client


@pytest.fixture(scope="session")
def event_loop() -> Iterable[AbstractEventLoop]:
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()
