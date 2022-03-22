FROM python:3.10-slim as build
ENV POETRY_VERSION=1.1.13

RUN pip install poetry==$POETRY_VERSION
COPY ./pyproject.toml ./poetry.lock ./
RUN poetry export -f requirements.txt --output requirements.txt

FROM python:3.10-slim
ENV PYTHONPATH=$PYTHONPATH:/app/src \
    PATH=$PATH:/home/app/.local/bin
RUN apt-get update && apt-get install -y curl

RUN addgroup --system app && adduser --system --group app
USER app

WORKDIR /app

COPY --from=build ./requirements.txt .
RUN pip install -r requirements.txt && pip install uvloop==0.16.0

COPY ./src ./src
COPY alembic.ini ./
ENTRYPOINT ["uvicorn", "app:create_app", "--factory", "--loop", "uvloop", "--host", "0.0.0.0", "--port", "8000"]
