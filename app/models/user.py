from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from app.models import users_enum


class User(BaseModel):
    id : UUID = Field(default_factory=uuid4)
    name : str
    email : str
    password : str
    role : users_enum.UserRole

    class CreateUser(BaseModel):
        name: str
        email: str
        password: str
        role: str

    class UpdateUser(BaseModel):
        name: Optional[str] = None
        email: Optional[str] = None
        password: Optional[str] = None

