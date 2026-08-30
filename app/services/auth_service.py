from typing import ClassVar
from uuid import UUID

from fastapi import HTTPException

from app.repositories.in_memory_user_repository import InMemoryUserRepository
from app.models.user import User
from app.repositories.user_repository import UserRepository


class AuthService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, request : User.CreateUser) -> User.CreateUserRespone:
        if request.password == "" or request.email == "" or request.name == "":
            raise HTTPException(status_code=400, detail="All fields are required")
        if len(request.password) < 8:
            raise HTTPException(status_code=400, detail="Password is too short")
        user = User(
            name=request.name,
            email=request.email,
            password=request.password,
            role=request.role,
        )
        self.repository.save_user(user)
        response = User.CreateUserRespone(id=user.id, name=user.name, email=user.email, role=user.role,)
        return response

    def login_user(self, request : User.LoginUser) -> User.LoginRespone:
        if request.password == "" or request.email == "":
            raise HTTPException(status_code=400, detail="All fields are required")
        user : User = self.repository.get_user_by_email(request.email)
        if user is not None and user.password == request.password:
            response = User.LoginRespone(
                message="login successful"
            )
            return response
        raise HTTPException(status_code=400, detail="Invalid Credentials")

    def logout(self, request: User.Logout) -> User.LogoutRespone:
        user = self.repository.get_user_by_email(request.email)
        if user is not None:
            response = User.LogoutRespone(
                message="logout successful"
            )
            return response
        raise HTTPException(status_code=400, detail="Email not found")

    def update_user(self, request : User.UpdateUser) -> User.UpdateUserRespone:
        if request.password == "" or request.email == "" or request.name == "":
            raise HTTPException(status_code=400, detail="All fields are required")
        if len(request.password) < 8:
            raise HTTPException(status_code=400, detail="Password is too short")
        user = User(
            name=request.name,
            email=request.email,
            password=request.password,
        )
        self.repository.UserRepository.update_user(user)
        response = User.UpdateUserRespone(id=user.id, name=user.name, email=user.email, role=user.role,)
        return response


    def delete_user(self, user_id : UUID) -> User.DeleteUserResponse:
        user : User = self.repository.get_user_by_id(user_id)
        if user is None:
            raise HTTPException(status_code=400, detail="User id is invalid")
        self.repository.delete_user(user)
        response = User.DeleteUserResponse(message="Account deleted successfully")
        return response


    def get_user_information(self, user_id : UUID) -> User.GetUserInfoRespone:
        user : User = self.repository.get_user_by_id(user_id)
        if user is None:
            raise HTTPException(status_code=400, detail="User id is invalid")
        response = User.GetUserInfoRespone(id=user.id, name=user.name, email=user.email,role=user.role,)
        return response


    def get_count(self):
        return self.repository.get_list_of_user()





