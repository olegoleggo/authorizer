from app.utils.generate_uuid import generate_uuid
from app.utils.generate_hash import generate_hash
from pydantic import BaseModel, Field
from uuid import UUID
from enum import Enum
from datetime import datetime


class TypeGender(str, Enum):
    male = 'male'
    female = 'female'


class SaveCustomUser(BaseModel):
    id: UUID = Field(default=generate_uuid())
    gender: TypeGender
    date_birth: datetime
    avatar: str
    name: str
    surname: str
    lastname: str
    qr_code: str
