from fastapi import FastAPI

from middleware import CommitSessionMiddleware


def create_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(CommitSessionMiddleware)

    @app.get("/healthcheck")
    def healthcheck() -> None:
        pass

    return app
