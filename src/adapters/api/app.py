from fastapi import FastAPI

import sentry
from adapters.api import books

from .middleware import CommitSessionMiddleware


def create_app() -> FastAPI:
    sentry.init_sentry()
    app = FastAPI()

    app.include_router(books.router)

    app.add_middleware(CommitSessionMiddleware)

    @app.get("/health")
    async def healthcheck() -> None:
        return None

    return app
