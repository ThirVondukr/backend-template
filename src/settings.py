from pydantic import BaseSettings


class DatabaseSettings(BaseSettings):
    class Config:
        env_prefix = "database_"

    driver: str = "postgresql+asyncpg"
    database: str = "database"
    username: str = "postgres"
    password: str = "password"
    host: str = "postgres"

    echo: bool = False

    @property
    def url(self) -> str:
        return f"{self.driver}://{self.username}:{self.password}@{self.host}/{self.database}"

    @property
    def alembic_url(self) -> str:
        return self.url.replace("+asyncpg", "")


db = DatabaseSettings()
