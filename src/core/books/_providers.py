import aioinject

from core.types import Providers

from .commands import BookCreateCommand
from .queries import BookGetQuery
from .repositories import BookRepository
from .services import BookService

providers: Providers = [
    aioinject.Callable(BookRepository),
    aioinject.Callable(BookService),
    aioinject.Callable(BookGetQuery),
    aioinject.Callable(BookCreateCommand),
]
