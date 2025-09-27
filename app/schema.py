import datetime
from pydantic import BaseModel


class IdResponse(BaseModel):
    id: int


class CreateAdvRequest(BaseModel):
    title: str
    description: str
    price: int
    owner: str


class GetAdvResponse(BaseModel):
    id: int
    title: str
    description: str
    price: int
    owner: str
    date: datetime.datetime


class SearchAdvResponse(BaseModel):
    advertisements: list[int]


class UpdateAdvRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    price: int | None = None
    owner: str | None = None
