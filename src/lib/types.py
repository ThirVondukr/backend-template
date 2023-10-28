from collections.abc import Iterable
from typing import Any, TypeAlias

from aioinject import Provider

Providers: TypeAlias = Iterable[Provider[Any]]
