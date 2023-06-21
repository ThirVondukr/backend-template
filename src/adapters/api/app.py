from fastapi import FastAPI

import sentry
from adapters.api import books
from adapters.graphql.app import create_graphql_app

from .middleware import CommitSessionMiddleware


def create_app() -> FastAPI:
    sentry.init_sentry()
    app = FastAPI()

    app.include_router(books.router)

    app.add_middleware(CommitSessionMiddleware)

    @app.get("/health")
    async def healthcheck() -> None:
        return None

    app.mount("/graphql", create_graphql_app())

    return app
