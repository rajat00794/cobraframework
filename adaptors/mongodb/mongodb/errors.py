from pydantic import BaseModel


class Errors(BaseModel):
    error: str
    model: str
