from typing import Annotated

import strawberry
from result import Err

from adapters.graphql.errors import EntityAlreadyExistsErrorGQL
from core.books.commands import BookCreateCommand
from core.books.exceptions import BookAlreadyExistsError
from core.books.services import BookService
from db.dependencies import create_session

from ._inputs import BookCreateInput
from ._payloads import BookCreatePayload
from .types import BookGQL


@strawberry.type
class BookMutation:
    @strawberry.mutation
    async def create_book(
        self,
        input_: Annotated[BookCreateInput, strawberry.argument(name="input")],
    ) -> BookCreatePayload:
        async with create_session() as session:
            command = BookCreateCommand(book_service=BookService(session=session))
            result = await command.execute(dto=input_.to_dto())

        if isinstance(result, Err):
            match result.err_value:
                case BookAlreadyExistsError():
                    return BookCreatePayload(
                        result=None,
                        error=EntityAlreadyExistsErrorGQL(),
                    )

        return BookCreatePayload(
            result=BookGQL.from_orm(result.ok_value),
            error=None,
        )
