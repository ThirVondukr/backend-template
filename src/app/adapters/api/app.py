import contextlib
from collections.abc import AsyncIterator, Iterable

from aioinject.ext.fastapi import AioInjectMiddleware
from fastapi import APIRouter, FastAPI

from app import telemetry
from app.adapters.api import books
from app.adapters.graphql.app import create_graphql_app
from app.core.di import create_container

_routers: Iterable[APIRouter] = [
    books.router,
]


def create_app() -> FastAPI:
    telemetry.setup_telemetry()
    container = create_container()

    @contextlib.asynccontextmanager
    async def lifespan(_: FastAPI) -> AsyncIterator[None]:
        async with contextlib.aclosing(container):
            yield

    app = FastAPI(lifespan=lifespan)
    app.add_middleware(AioInjectMiddleware, container=container)

    for router in _routers:
        app.include_router(router)

    @app.get("/health")
    async def healthcheck() -> None:
        return None

    app.mount("/graphql", create_graphql_app())

    return app
