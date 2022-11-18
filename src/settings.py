import functools
from typing import TypeVar

from pydantic import BaseSettings, RedisDsn

TSettings = TypeVar("TSettings", bound=BaseSettings)


def get_settings(cls: type[TSettings]) -> TSettings:
    return cls()


get_settings = functools.lru_cache(get_settings)  # Mypy moment


class DatabaseSettings(BaseSettings):
    class Config:
        env_prefix = "database_"

    driver: str = "postgresql+asyncpg"
    name: str
    username: str
    password: str
    host: str

    echo: bool = False

    @property
    def url(self) -> str:
        return (
            f"{self.driver}://{self.username}:{self.password}@{self.host}/{self.name}"
        )

    @property
    def alembic_url(self) -> str:
        return self.url.replace("+asyncpg", "")


class CelerySettings(BaseSettings):
    broker_url: RedisDsn
    backend_url: RedisDsn

    class Config:
        env_prefix = "celery_"
