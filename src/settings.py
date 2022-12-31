import functools
from typing import TypeVar
from urllib.parse import quote_plus

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
        password = quote_plus(self.password)
        return f"{self.driver}://{self.username}:{password}@{self.host}/{self.name}"


class CelerySettings(BaseSettings):
    broker_url: RedisDsn
    backend_url: RedisDsn

    class Config:
        env_prefix = "celery_"
