from pydantic import BaseModel
from typing import Optional


class Users(BaseModel):
    id: int
    surname: str
    name: str
    patronymic: str
    tel1: str
    description: Optional[str] = None
    addTime: str