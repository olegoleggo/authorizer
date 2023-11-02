from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class GetCustomUser(BaseModel):
    id: UUID
    gender: str
    date_birthday: datetime
    avatar: str  # ссылка на аватурку
    name: str
    surname: str
    lastname: str
    qr: str  # ссылка на qr код
