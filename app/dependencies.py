from fastapi import Depends
from app.repositories.event_repository import EventRepository
from app.repositories.in_memory_event_repository import InMemoryEventRepository
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService

from app.services.event_service import EventService
from app.repositories.booking_repository import BookingRepository
from app.services.booking_service import BookingService
from app.repositories.in_memory_user_repository import InMemoryUserRepository

_repository = InMemoryEventRepository()
_auth_repository = InMemoryUserRepository()

def get_event_repository() -> EventRepository:
    return _repository

def get_event_service(
    repository: EventRepository = Depends(get_event_repository)
) -> EventService:
    return EventService(repository)

def get_user_repository() -> UserRepository:
    return _auth_repository

def get_user_service(
        repository: UserRepository = Depends(get_user_repository)
) -> AuthService:
    return AuthService(repository)

def get_booking_repository() -> BookingRepository:
    return _repository

def get_booking_service(
        repository: BookingRepository = Depends(get_booking_repository)
) -> BookingService:
    return BookingService(repository)