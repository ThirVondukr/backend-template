from typing import Annotated

from aioinject import Inject
from aioinject.ext.fastapi import inject
from fastapi import APIRouter, HTTPException, status
from result import Err

from core.books.commands import BookCreateCommand
from core.books.dto import BookCreateDTO
from core.books.errors import BookAlreadyExistsError
from core.books.queries import GetBookQuery

from .schema import BookCreateSchema, BookSchema

router = APIRouter(
    tags=["books"],
    prefix="/books",
)


@router.post(
    "",
    responses={
        status.HTTP_201_CREATED: {"model": BookSchema},
    },
    status_code=status.HTTP_201_CREATED,
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
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    return BookSchema.model_validate(book.ok_value)


@router.get(
    "/{book_id}",
    responses={
        status.HTTP_200_OK: {"model": BookSchema},
        status.HTTP_404_NOT_FOUND: {"description": "Book not found"},
    },
)
@inject
async def books_retrieve(
    book_id: int,
    book_query: Annotated[GetBookQuery, Inject],
) -> BookSchema:
    book = await book_query.execute(book_id=book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return BookSchema.model_validate(book)
