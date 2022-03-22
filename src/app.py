from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI()

    @app.get("/healthcheck")
    def healthcheck() -> None:
        pass

    return app
