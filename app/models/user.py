from dataclasses import field
from uuid import UUID, uuid4

from pydantic import BaseModel

from app.models import users_enum


class User(BaseModel):
    id : UUID = field(default_factory=uuid4)
    name : str
    email : str
    password : str
    role : users_enum.UserRole