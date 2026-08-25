from pydantic import BaseModel

from app.models import user
from app.models.user import User
from app.repositories import in_memory_user_repository, user_repository


class AuthService(BaseModel):

    repository = user_repository

    def create_user(self, request : user.CreateUser):
        user = User(
            name=request.name,
            email=request.email,
            password=request.password,
            role=request.role,
        )
        self.repository.UserRepository.save_user(user)
        return user

    def update_user(self, request : User.UpdateUser):
        user = User(
            name=request.name,
            email=request.email,
            password=request.password,
        )
        self.repository.UserRepository.update_user(user)
        return user




