from fastapi import Depends
from app.repositories.event_repository import EventRepository
from app.repositories.in_memory_event_repository import InMemoryEventRepository
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService

from app.services.event_service import EventService

_repository = InMemoryEventRepository()

def get_event_repository() -> EventRepository:
    return _repository

def get_event_service(
    repository: EventRepository = Depends(get_event_repository)
) -> EventService:
    return EventService(repository)

def get_user_repository() -> UserRepository:
    return _repository

def get_user_service(
        repository: UserRepository = Depends(get_user_repository)
) -> AuthService:
    return AuthService(repository)