from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from app.models import users_enum


class User(BaseModel):
    id : UUID = Field(default_factory=uuid4)
    name : str
    email : str
    password : str
    role : users_enum.UserRole