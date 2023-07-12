import pydantic
from pydantic import ConfigDict

from adapters.api.schema import BaseSchema


class BookSchema(BaseSchema):
    model_config = ConfigDict(title="Book")

    id: int
    title: str


class BookCreateSchema(BaseSchema):
    model_config = ConfigDict(title="BookCreate")

    title: str = pydantic.Field(max_length=255)
