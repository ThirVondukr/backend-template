from pydantic import BaseModel
from pydantic.generics import GenericModel


def _snake_to_camel(name: str) -> str:
    first, *rest = name.split("_")
    return first + "".join(map(str.capitalize, rest))


class BaseSchema(BaseModel):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        alias_generator = _snake_to_camel


class GenericSchema(GenericModel):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        alias_generator = _snake_to_camel
