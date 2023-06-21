from typing import Annotated

import strawberry

from adapters.graphql.apps.books.types import BookGQL
from core.books.queries import GetBookQuery
from core.books.services import BookService
from db.dependencies import create_session


@strawberry.type
class BookQuery:
    @strawberry.field
    async def book(
        self,
        id_: Annotated[strawberry.ID, strawberry.argument(name="id")],
    ) -> BookGQL | None:
        try:
            int_id = int(id_)
        except ValueError:
            return None

        async with create_session() as session:
            command = GetBookQuery(book_service=BookService(session))
            book = await command.execute(book_id=int_id)

        return BookGQL.from_orm_optional(book)
