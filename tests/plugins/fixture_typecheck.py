from typing import Any

import typeguard
from _pytest.python import Function
from _pytest.runner import CallInfo


def pytest_runtest_makereport(item: Function, call: CallInfo[Any]) -> None:
    if call.when == "call":
        for fixture_name, ty in item.obj.__annotations__.items():
            if fixture_name not in item.funcargs:
                continue
            typeguard.check_type(item.funcargs[fixture_name], ty)
