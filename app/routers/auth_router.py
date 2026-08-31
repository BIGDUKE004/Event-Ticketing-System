from uuid import UUID

from fastapi import APIRouter, status, Depends

from app.models.user import *
from app.services.auth_service import AuthService
from app.dependencies import get_user_service

router = APIRouter(prefix="/auth", tags=["SignUp/SignIn"])



@router.post("/register", response_model=CreateUserRespone, status_code=status.HTTP_201_CREATED)
def register(request: CreateUser, service : AuthService = Depends(get_user_service)):
    return service.create_user(request)


@router.post("/login", response_model=LoginRespone)
def login(request: LoginUser, service : AuthService = Depends(get_user_service)):
    return service.login_user(request)


@router.post("/logout", response_model=LogoutRespone)
def logout(request: Logout, service : AuthService = Depends(get_user_service)):
    return service.logout(request)


@router.put("/update", response_model=UpdateUserRespone)
def update_user(request: UpdateUser, service : AuthService = Depends(get_user_service)):
    return service.update_user(request)


@router.delete("/delete/{user_id}", response_model=DeleteUserResponse)
def delete_user(user_id : UUID, service : AuthService = Depends(get_user_service)):
    service.delete_user(user_id)


@router.get("/GetInformation/{user_id}", response_model=GetUserInfoRespone)
def get_user_information(user_id : UUID, service : AuthService = Depends(get_user_service)):
    return service.get_user_information(user_id)