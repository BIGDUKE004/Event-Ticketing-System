from typing import ClassVar

from fastapi import HTTPException

from app.repositories.in_memory_user_repository import InMemoryUserRepository
from app.models.user import User


class AuthService:

    repository : ClassVar = InMemoryUserRepository()

    def create_user(self, request : User.CreateUser) -> User.CreateUserRespone:
        if request.password == "" or request.email == "" or request.role == "" or request.name == "":
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


    def update_user(self, request : User.UpdateUser) -> User.UpdateUserRespone:
        if request.password == "" or request.email == "" or request.role == "" or request.name == "":
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


    def delete_user(self, request : User.DeleteUser) -> None:
        for users in self.repository:
            if users.id != request.id:
                raise HTTPException(status_code=400, detail="User id is invalid")
        self.repository.UserRepository.delete_user(request.id)


    def get_user_information(self, request : User.GetUserInfo) -> User.GetUserInfoRespone:
        for users in self.repository:
            if users.id != request.id:
                raise HTTPException(status_code=400, detail="User id is invalid")
        user : User = self.repository.UserRepository.get_user_by_id(request.id)
        response = User.GetUserInfoRespone(id=user.id, name=user.name, email=user.email,role=user.role,)
        return response


    def get_count(self):
        return self.repository.get_list_of_user()





