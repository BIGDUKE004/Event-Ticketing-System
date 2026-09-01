from fastapi import HTTPException

from app.models.user import *
from app.repositories.user_repository import UserRepository
from app.database_models.user import User


class AuthService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, request : CreateUser) -> CreateUserRespone:
        if request.password == "" or request.email == "" or request.name == "":
            raise HTTPException(status_code=400, detail="All fields are required")
        if len(request.password) < 8:
            raise HTTPException(status_code=400, detail="Password is too short")
        user = User(
            name=request.name,
            email=request.email,
            password=request.password,
            role=request.role,
            isLoggedIn=request.isLoggedIn,
        )
        self.repository.save_user(user)
        response = CreateUserRespone(id=user.id, name=user.name, email=user.email, role=user.role,)
        return response

    def login_user(self, request : LoginUser) -> LoginRespone:
        if request.password == "" or request.email == "":
            raise HTTPException(status_code=400, detail="All fields are required")
        user = self.repository.get_user_by_email(request.email)
        if user is not None and user.password == request.password:
            user.isLoggedIn = True
            self.repository.update_user(user)
            response = LoginRespone(
                message="login successful"
            )
            return response
        raise HTTPException(status_code=400, detail="Invalid Credentials")

    def logout(self, request: Logout) -> LogoutRespone:
        user = self.repository.get_user_by_email(request.email)
        if user is not None:
            user.isLoggedIn = False
            self.repository.update_user(user)
            response = LogoutRespone(
                message="logout successful"
            )
            return response
        raise HTTPException(status_code=400, detail="Email not found")

    def update_user(self, request : UpdateUser) -> UpdateUserRespone:
        if request.password == "" or request.email == "" or request.name == "":
            raise HTTPException(status_code=400, detail="All fields are required")
        if len(request.password) < 8:
            raise HTTPException(status_code=400, detail="Password is too short")
        user = User(
            name=request.name,
            email=request.email,
            password=request.password,
        )
        self.repository.update_user(user)
        response = UpdateUserRespone(id=user.id, name=user.name, email=user.email, role=user.role,)
        return response


    def delete_user(self, user_id : UUID) -> DeleteUserResponse:
        user = self.repository.get_user_by_id(user_id)
        if user is None:
            raise HTTPException(status_code=400, detail="User id is invalid")
        self.repository.delete_user(user)
        response = DeleteUserResponse(message="Account deleted successfully")
        return response


    def get_user_information(self, user_id : UUID) -> GetUserInfoRespone:
        user = self.repository.get_user_by_id(user_id)
        if user is None:
            raise HTTPException(status_code=400, detail="User id is invalid")
        response = GetUserInfoRespone(id=user.id, name=user.name, email=user.email,role=user.role,)
        return response


    def get_count(self):
        return self.repository.get_list_of_user()





