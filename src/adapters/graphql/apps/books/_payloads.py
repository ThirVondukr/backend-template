import strawberry

from adapters.graphql.apps.books.types import BookGQL
from adapters.graphql.errors import EntityAlreadyExistsErrorGQL

BookCreateErrors = strawberry.union(
    name="BookCreateErrors",
    types=(EntityAlreadyExistsErrorGQL,),
)


@strawberry.type(name="BookCreatePayload")
class BookCreatePayload:
    result: BookGQL | None
    error: BookCreateErrors | None
