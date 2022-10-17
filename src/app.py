from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from apps import books
from db.dependencies import get_session
from middleware import CommitSessionMiddleware


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(books.router)

    app.add_middleware(CommitSessionMiddleware)

    @app.get("/healthcheck")
    async def healthcheck(
        session: AsyncSession = Depends(get_session),
    ) -> None:
        await session.execute(text("select 1"))

    return app
