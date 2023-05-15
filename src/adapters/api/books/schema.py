import pydantic

from adapters.api.schema import BaseSchema


class BookSchema(BaseSchema):
    class Config:
        title = "Book"

    id: int
    title: str


class BookCreateSchema(BaseSchema):
    class Config:
        title = "BookCreate"

    title: str = pydantic.Field(max_length=255)
