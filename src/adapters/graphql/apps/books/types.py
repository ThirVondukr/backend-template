from typing import Self

import strawberry

from adapters.graphql.dto import DTOMixin
from db.models import Book


@strawberry.type(name="Book")
class BookGQL(DTOMixin[Book]):
    id: strawberry.ID
    title: str

    @classmethod
    def from_orm(cls, model: Book) -> Self:
        return cls(
            id=strawberry.ID(str(model.id)),
            title=model.title,
        )
