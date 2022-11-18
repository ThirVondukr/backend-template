from fastapi import APIRouter, Depends, HTTPException, status

from core.books.dto import BookCreateDto
from core.books.exceptions import BookAlreadyExistsError
from core.books.services import BookService

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
async def books_create(
    schema: BookCreateSchema,
    book_service: BookService = Depends(),
) -> BookSchema:
    try:
        book = await book_service.create(dto=BookCreateDto.from_orm(schema))
    except BookAlreadyExistsError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST) from e

    return BookSchema.from_orm(book)


@router.get(
    "/{book_id}",
    responses={
        status.HTTP_200_OK: {"model": BookSchema},
        status.HTTP_404_NOT_FOUND: {"description": "Book not found"},
    },
)
async def books_retrieve(
    book_id: int,
    book_service: BookService = Depends(),
) -> BookSchema:
    book = await book_service.get_one(book_id=book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return BookSchema.from_orm(book)
