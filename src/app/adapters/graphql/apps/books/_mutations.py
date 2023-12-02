from typing import Annotated

import strawberry
from aioinject import Inject
from aioinject.ext.strawberry import inject
from result import Err

from app.adapters.graphql.errors import EntityAlreadyExistsErrorGQL
from app.core.domain.books.commands import BookCreateCommand
from app.core.domain.books.errors import BookAlreadyExistsError

from ._inputs import BookCreateInput
from ._payloads import BookCreatePayload
from .types import BookGQL


@strawberry.type
class BookMutation:
    @strawberry.mutation
    @inject
    async def create_book(
        self,
        input_: Annotated[BookCreateInput, strawberry.argument(name="input")],
        command: Annotated[BookCreateCommand, Inject],
    ) -> BookCreatePayload:
        result = await command.execute(dto=input_.to_dto())

        if isinstance(result, Err):
            match result.err_value:
                case BookAlreadyExistsError():  # pragma: no branch
                    return BookCreatePayload(
                        result=None,
                        error=EntityAlreadyExistsErrorGQL(),
                    )

        return BookCreatePayload(
            result=BookGQL.from_dto(result.ok_value),
            error=None,
        )
