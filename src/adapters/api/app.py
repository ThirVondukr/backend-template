import contextlib
from collections.abc import AsyncIterator, Iterable

from aioinject.ext.fastapi import InjectMiddleware
from fastapi import APIRouter, FastAPI

import sentry
from adapters.api import books
from adapters.graphql.app import create_graphql_app
from core.di import create_container

_routers: Iterable[APIRouter] = [
    books.router,
]


def create_app() -> FastAPI:
    sentry.init_sentry()
    container = create_container()

    @contextlib.asynccontextmanager
    async def lifespan(_: FastAPI) -> AsyncIterator[None]:
        async with contextlib.aclosing(container):
            yield

    app = FastAPI(lifespan=lifespan)
    app.add_middleware(InjectMiddleware, container=container)

    for router in _routers:
        app.include_router(router)

    @app.get("/health")
    async def healthcheck() -> None:
        return None

    app.mount("/graphql", create_graphql_app())

    return app
