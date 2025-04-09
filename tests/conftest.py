import pkgutil
from datetime import datetime
from typing import cast

import dotenv
import pytest
from _pytest.fixtures import SubRequest

import tests.plugins
from lib.time import utc_now

dotenv.load_dotenv(".env")

pytest_plugins = [
    "anyio",
    "sqlalchemy_pytest.database",
    *(
        mod.name
        for mod in pkgutil.walk_packages(
            tests.plugins.__path__,
            prefix="tests.plugins.",
        )
        if not mod.ispkg
    ),
]


@pytest.fixture(scope="session", autouse=True)
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture
def now() -> datetime:
    return utc_now()


@pytest.fixture(params=[0, 1, 10])
def collection_size(request: SubRequest) -> int:
    return cast("int", request.param)
