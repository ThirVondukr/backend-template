from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from apps.books.schema import BookCreateSchema, BookSchema
from db.dependencies import get_session
from db.models import Book

router = APIRouter(
    tags=["books"],
    prefix="/books",
)


@router.post(
    "",
    responses={status.HTTP_201_CREATED: {"model": BookSchema}},
    status_code=status.HTTP_201_CREATED,
)
async def books_create(
    schema: BookCreateSchema, session: AsyncSession = Depends(get_session)
) -> BookSchema:
    book = Book(**schema.dict())
    session.add(book)
    await session.flush()
    await session.refresh(book)
    return BookSchema.from_orm(book)
