from pydantic import BaseModel, ConfigDict


def _snake_to_camel(name: str) -> str:
    first, *rest = name.split("_")
    return first + "".join(map(str.capitalize, rest))


class BaseSchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=_snake_to_camel,
    )
