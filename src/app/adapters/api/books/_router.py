from http import HTTPStatus
from typing import Annotated

from aioinject import Inject
from aioinject.ext.fastapi import inject
from fastapi import APIRouter, HTTPException
from result import Err

from app.core.books.commands import BookCreateCommand
from app.core.books.dto import BookCreateDTO
from app.core.books.errors import BookAlreadyExistsError
from app.core.books.queries import BookGetQuery

from .schema import BookCreateSchema, BookSchema

router = APIRouter(
    tags=["books"],
    prefix="/books",
)


@router.post(
    "",
    responses={
        HTTPStatus.CREATED: {"model": BookSchema},
    },
    status_code=HTTPStatus.CREATED,
)
@inject
async def books_create(
    schema: BookCreateSchema,
    command: Annotated[BookCreateCommand, Inject],
) -> BookSchema:
    book = await command.execute(dto=BookCreateDTO.model_validate(schema))
    if isinstance(book, Err):
        match book.err_value:
            case BookAlreadyExistsError():  # pragma: no branch
                raise HTTPException(status_code=HTTPStatus.BAD_REQUEST)

    return BookSchema.model_validate(book.ok_value)


@router.get(
    "/{book_id}",
    responses={
        HTTPStatus.OK: {"model": BookSchema},
        HTTPStatus.NOT_FOUND: {"description": "Book not found"},
    },
)
@inject
async def books_retrieve(
    book_id: int,
    book_query: Annotated[BookGetQuery, Inject],
) -> BookSchema:
    book = await book_query.execute(book_id=book_id)
    if not book:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)

    return BookSchema.model_validate(book)
