from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from settings import DatabaseSettings, get_settings

_settings = get_settings(DatabaseSettings)

engine = create_async_engine(
    _settings.url,
    future=True,
    pool_size=20,
    pool_pre_ping=True,
    pool_use_lifo=True,
    echo=_settings.echo,
)
async_sessionmaker = sessionmaker(
    future=True,
    class_=AsyncSession,
    bind=engine,
    expire_on_commit=False,
)
