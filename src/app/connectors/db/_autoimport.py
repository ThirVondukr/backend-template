import importlib
import pkgutil
from types import ModuleType


def collect_models(root: ModuleType, module_names: tuple[str] = ("models",)) -> None:
    """
    Import modules that are likely to contain sqlalchemy models.

    In order for alembic to generate migrations models should be loaded into memory,
    and hence we need to execute/import modules containing them.
    """
    for module in pkgutil.walk_packages(root.__path__, prefix=f"{root.__name__}."):
        *_, module_name = module.name.split(".")
        if module_name in module_names:
            importlib.import_module(name=module.name)
