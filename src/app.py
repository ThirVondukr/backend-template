from fastapi import FastAPI

from apps import books
from middleware import CommitSessionMiddleware


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(books.router)

    app.add_middleware(CommitSessionMiddleware)

    @app.get("/health")
    async def healthcheck() -> None:
        return None

    return app
