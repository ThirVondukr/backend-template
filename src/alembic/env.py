import asyncio
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from sqlalchemy.engine import Connectable, Connection
from sqlalchemy.ext.asyncio import AsyncEngine

import db.models  # noqa: F401
import sentry
from alembic import context
from db import Base
from settings import DatabaseSettings, get_settings

sentry.init_sentry()
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

if not config.get_main_option("sqlalchemy.url"):
    config.set_main_option("sqlalchemy.url", get_settings(DatabaseSettings).url)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,
        compare_server_default=True,
    )

    with context.begin_transaction():
        context.run_migrations()


async def do_run_migrations_async(connectable: Connectable) -> None:
    async with connectable.connect() as conn:
        await conn.run_sync(do_run_migrations)


def run_migrations() -> None:
    connectable = context.config.attributes.get("connection")
    if not connectable:
        connectable = AsyncEngine(
            engine_from_config(
                config.get_section(config.config_ini_section),
                poolclass=pool.NullPool,
                future=True,
            ),
        )
    if isinstance(connectable, AsyncEngine):
        asyncio.run(do_run_migrations_async(connectable))
    else:
        do_run_migrations(connectable)


run_migrations()
