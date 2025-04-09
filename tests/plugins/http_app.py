from collections.abc import AsyncIterator

import httpx
import pytest
from asgi_lifespan import LifespanManager
from fastapi import FastAPI


@pytest.fixture(scope="session")
async def http_app() -> AsyncIterator[FastAPI]:
    from app.adapters.api.app import create_app

    app = create_app()
    async with LifespanManager(app=app):
        yield app


@pytest.fixture
async def http_client(http_app: FastAPI) -> AsyncIterator[httpx.AsyncClient]:
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(
            app=http_app,
        ),
        base_url="http://test",
    ) as client:
        yield client
