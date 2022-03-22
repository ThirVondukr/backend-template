from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

import settings

engine = create_async_engine(
    settings.db.url,
    future=True,
    pool_size=20,
    pool_pre_ping=True,
    pool_use_lifo=True,
    echo=settings.db.echo,
)
async_sessionmaker = sessionmaker(
    future=True,
    class_=AsyncSession,
    bind=engine,
    expire_on_commit=False,
)
Base = declarative_base()
