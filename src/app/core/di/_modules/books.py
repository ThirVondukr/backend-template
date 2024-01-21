import aioinject

from app.core.domain.books.commands import BookCreateCommand
from app.core.domain.books.queries import BookGetQuery
from app.core.domain.books.repositories import BookRepository
from app.core.domain.books.services import BookService
from lib.types import Providers

providers: Providers = [
    aioinject.Scoped(BookRepository),
    aioinject.Scoped(BookService),
    aioinject.Scoped(BookGetQuery),
    aioinject.Scoped(BookCreateCommand),
]
