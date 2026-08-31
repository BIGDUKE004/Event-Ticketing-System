from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field
from sqlalchemy.engine import default

from app.models import users_enum

class CreateUser(BaseModel):
    name: str
    email: str
    password: str
    role: str
    isLoggedIn: bool = False

class LoginUser(BaseModel):
    email: str
    password: str

class Logout(BaseModel):
    email: str

class LoginRespone(BaseModel):
    message: str

class LogoutRespone(BaseModel):
    message: str

class UpdateUser(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class DeleteUser(BaseModel):
    id: UUID

class DeleteUserResponse(BaseModel):
    message: str

class GetUserInfo(BaseModel):
    id: UUID

class CreateUserRespone(BaseModel):
    id: UUID
    name: str
    email: str
    role: str

class UpdateUserRespone(BaseModel):
    id: UUID
    name: str
    email: str
    role: str

class GetUserInfoRespone(BaseModel):
    id: UUID
    name: str
    email: str
    role: str

