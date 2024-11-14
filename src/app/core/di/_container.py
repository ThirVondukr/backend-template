import functools
import importlib
import pkgutil
from collections.abc import Sequence
from types import ModuleType

import aioinject
from aioinject import Provider

from . import _modules


def _autodiscover_providers(
    module: ModuleType,
    attr_name: str,
    *,
    raise_error: bool = True,
) -> Sequence[Provider[object]]:
    result: list[Provider[object]] = []
    for submodule_info in pkgutil.walk_packages(module.__path__, f"{module.__name__}."):
        if submodule_info.ispkg:  # pragma: no cover
            continue

        submodule = importlib.import_module(submodule_info.name)
        module_providers = getattr(submodule, attr_name, None)
        if module_providers is None:  # pragma: no cover
            if raise_error:
                msg = (
                    f"Module {submodule_info.name} does not have {attr_name} attribute"
                )
                raise ValueError(msg)
            continue
        result.extend(module_providers)
    return result


@functools.cache
def create_container() -> aioinject.Container:
    container = aioinject.Container()

    for provider in _autodiscover_providers(module=_modules, attr_name="providers"):
        container.register(provider)

    return container
