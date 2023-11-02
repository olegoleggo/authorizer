from app.utils.generate_uuid import generate_uuid
from app.utils.generate_hash import generate_hash
from uuid import UUID
from pydantic import BaseModel


class GetStudent(BaseModel):
    id: UUID
    name: str
    group: str
    university: str
    last_name: str
