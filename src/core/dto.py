from pydantic import BaseModel


class BaseDTO(BaseModel):
    class Config:
        orm_mode = True
