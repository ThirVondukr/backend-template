import functools
import itertools
from collections.abc import Iterable
from typing import Any

import aioinject
from aioinject import Provider

from app import db
from app.core import books

modules: Iterable[Iterable[Provider[Any]]] = [
    db.providers,
    books.providers,
]


@functools.cache
def create_container() -> aioinject.Container:
    container = aioinject.Container()

    for provider in itertools.chain.from_iterable(modules):
        container.register(provider)

    return container
