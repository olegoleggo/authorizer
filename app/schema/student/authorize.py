from pydantic import BaseModel
from uuid import UUID


class AuthorizerUserRequest(BaseModel):
    login: str
    password: str


class AuthorizerUserResponse(BaseModel):
    session_id: UUID

