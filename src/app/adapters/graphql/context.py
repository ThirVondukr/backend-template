import dataclasses
from typing import TypeVar

from fastapi.requests import Request
from fastapi.responses import Response
from fastapi.websockets import WebSocket
from strawberry.types import Info as StrawberryInfo

from .dataloaders import Dataloaders

T = TypeVar("T")


@dataclasses.dataclass(slots=True, kw_only=True)
class Context:
    request: Request | WebSocket
    response: Response | WebSocket
    loaders: Dataloaders


Info = StrawberryInfo[Context, None]
