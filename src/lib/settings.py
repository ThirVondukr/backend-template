import functools
from typing import TypeVar

import dotenv
from pydantic_settings import BaseSettings

TSettings = TypeVar("TSettings", bound=BaseSettings)


def get_settings(cls: type[TSettings]) -> TSettings:
    dotenv.load_dotenv()
    return cls()


get_settings = functools.lru_cache(get_settings)  # Mypy moment
