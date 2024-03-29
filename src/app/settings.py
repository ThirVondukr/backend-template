import enum
from urllib.parse import quote_plus

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class SentryEnvironment(enum.StrEnum):
    development = enum.auto()
    staging = enum.auto()
    production = enum.auto()


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="database_")

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


class SentrySettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="sentry_")

    dsn: str = ""
    environment: SentryEnvironment = SentryEnvironment.production
    traces_sample_rate: float = Field(default=1.0, ge=0.0, le=1.0)
