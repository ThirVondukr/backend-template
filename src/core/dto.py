from pydantic import BaseModel


class BaseDto(BaseModel):
    class Config:
        orm_mode = True
