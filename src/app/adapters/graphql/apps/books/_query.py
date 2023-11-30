from typing import Annotated

import strawberry
from aioinject import Inject
from aioinject.ext.strawberry import inject

from app.core.domain.books.queries import BookGetQuery

from .types import BookGQL


@strawberry.type
class BookQuery:
    @strawberry.field
    @inject
    async def book(
        self,
        id_: Annotated[strawberry.ID, strawberry.argument(name="id")],
        query: Annotated[BookGetQuery, Inject],
    ) -> BookGQL | None:
        try:
            int_id = int(id_)
        except ValueError:
            return None

        book = await query.execute(book_id=int_id)
        return BookGQL.from_orm_optional(book)
