from fastapi import HTTPException
from app.core.security import (
    verify_password,
    create_access_token, hash_password
)

from app.models.user import *
from app.repositories.user_repository import UserRepository
from app.database_models.user import User
from app.models.users_enum import UserRole

class AuthService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, request : CreateUser) -> CreateUserRespone:
        if request.password == "" or request.email == "" or request.name == "":
            raise HTTPException(status_code=400, detail="All fields are required")
        if len(request.password) < 8:
            raise HTTPException(status_code=400, detail="Password is too short")
        password = hash_password(request.password.strip())
        user = User(
            name=request.name.strip(),
            email=request.email.strip(),
            password=password,
            role=UserRole.CUSTOMER,
            isLoggedIn=False,
        )
        self.repository.save_user(user)
        response = CreateUserRespone(id=user.id, name=user.name, email=user.email, role=user.role,)
        return response

    def login_user(self, request: LoginUser) -> LoginRespone:
        if request.password == "" or request.email == "":
            raise HTTPException(status_code=400, detail="All fields are required")
        user = self.repository.get_user_by_email(request.email.strip())
        pass
        if user is not None and verify_password(
                request.password.strip(),
                user.password
        ):
            user.isLoggedIn = True
            self.repository.update_user(user)
            token = create_access_token(str(user.id))

            return LoginRespone(
                id=user.id,
                name=user.name,
                email=user.email,
                role=user.role,
                access_token=token,
            )
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





