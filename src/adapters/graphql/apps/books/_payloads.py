from typing import Annotated

import strawberry

from adapters.graphql.errors import EntityAlreadyExistsErrorGQL

from .types import BookGQL

BookCreateErrors = Annotated[
    EntityAlreadyExistsErrorGQL,
    strawberry.union(name="BookCreateErrors"),
]


@strawberry.type(name="BookCreatePayload")
class BookCreatePayload:
    result: BookGQL | None
    error: BookCreateErrors | None
