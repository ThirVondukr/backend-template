import dataclasses
from typing import TypeVar

from starlette.requests import Request
from starlette.responses import Response
from starlette.websockets import WebSocket
from strawberry.types import Info as StrawberryInfo

from .dataloaders import Dataloaders

T = TypeVar("T")


@dataclasses.dataclass(slots=True, kw_only=True)
class Context:
    request: Request | WebSocket
    response: Response | WebSocket
    loaders: Dataloaders


Info = StrawberryInfo[Context, None]
