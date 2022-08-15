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
Base.metadata.naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
