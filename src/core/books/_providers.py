import aioinject

from core.types import Providers

from .commands import BookCreateCommand
from .queries import GetBookQuery
from .services import BookService

providers: Providers = [
    aioinject.Callable(BookService),
    aioinject.Callable(GetBookQuery),
    aioinject.Callable(BookCreateCommand),
]
