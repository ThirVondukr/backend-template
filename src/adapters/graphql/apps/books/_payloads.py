from typing import Annotated

import strawberry

from adapters.graphql.apps.books.types import BookGQL
from adapters.graphql.errors import EntityAlreadyExistsErrorGQL

BookCreateErrors = Annotated[
    EntityAlreadyExistsErrorGQL,
    strawberry.union(name="BookCreateErrors"),
]


@strawberry.type(name="BookCreatePayload")
class BookCreatePayload:
    result: BookGQL | None
    error: BookCreateErrors | None
