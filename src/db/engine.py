from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from settings import DatabaseSettings, get_settings

_settings = get_settings(DatabaseSettings)

engine = create_async_engine(
    _settings.url,
    pool_size=20,
    pool_pre_ping=True,
    pool_use_lifo=True,
    echo=_settings.echo,
)
async_session_factory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)
