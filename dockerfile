FROM python:3.10-slim as build

RUN pip install pdm
COPY ./pyproject.toml ./pdm.lock ./
RUN pdm export --prod -f requirements -o requirements.txt

FROM python:3.10-slim
ENV PYTHONPATH=$PYTHONPATH:/app/src \
    PATH=$PATH:/home/app/.local/bin \
    PYTHONUNBUFFERED=1

RUN addgroup --system app && adduser --system --group app
USER app

WORKDIR /app

COPY --from=build ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src
COPY alembic.ini ./
ENTRYPOINT ["uvicorn", "app:create_app", "--factory", "--loop", "uvloop", "--host", "0.0.0.0", "--port", "8000"]
