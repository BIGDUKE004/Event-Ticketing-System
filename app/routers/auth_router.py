from uuid import UUID

from fastapi import APIRouter, status

from app.models.user import User
from app.repositories.in_memory_user_repository import InMemoryUserRepository
from app.services.auth_service import AuthService


router = APIRouter(prefix="/auth")

repository = InMemoryUserRepository()
service = AuthService(repository)


@router.post("/register", response_model=User.CreateUserRespone, status_code=status.HTTP_201_CREATED)
def register(request: User.CreateUser):
    return service.create_user(request)


@router.post("/login", response_model=User.LoginRespone)
def login(request: User.LoginUser):
    return service.login(request)


@router.post("/logout", response_model=User.LogoutRespone)
def logout(request: User.Logout):
    return service.logout(request)


@router.put("/update", response_model=User.UpdateUserRespone)
def update_user(request: User.UpdateUser):
    return service.update_user(request)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: UUID):
    request = User.DeleteUser(id=user_id)
    service.delete_user(request)


@router.get("/{user_id}", response_model=User.GetUserInfoRespone)
def get_user_information(user_id: UUID):
    request = User.GetUserInfo(id=user_id)
    return service.get_user_information(request)