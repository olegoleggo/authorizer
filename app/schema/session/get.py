from pydantic import BaseModel
from uuid import UUID


class GetSession(BaseModel):
    session_value: UUID
    active: bool
