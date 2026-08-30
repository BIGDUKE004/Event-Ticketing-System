from fastapi import Depends
from app.repositories.event_repository import EventRepository
from app.repositories.in_memory_event_repository import InMemoryEventRepository
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService
from app.services.event_service import EventService

from app.repositories.booking_repository import BookingRepository
from app.services.booking_service import BookingService
from app.repositories.in_memory_user_repository import InMemoryUserRepository

from app.repositories.in_memory_ticket_repository import InMemoryTicketRepository
from app.services.ticket_service import TicketService
from app.repositories.in_memory_ticket_type_repository import InMemoryTicketTypeRepository
from app.services.ticket_type_service import TicketTypeService


_repository = InMemoryEventRepository()
_auth_repository = InMemoryUserRepository()
_ticket_repository = InMemoryTicketRepository()
_ticket_type_repository = InMemoryTicketTypeRepository()

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

def get_ticket_repository() -> InMemoryTicketRepository:
    return _ticket_repository


def get_ticket_type_repository() -> InMemoryTicketTypeRepository:
    return _ticket_type_repository


def get_ticket_service(
    ticket_repository: InMemoryTicketRepository = Depends(get_ticket_repository),
    ticket_type_repository: InMemoryTicketTypeRepository = Depends(get_ticket_type_repository),
) -> TicketService:
    return TicketService(
        ticket_repository=ticket_repository,
        ticket_type_repository=ticket_type_repository,
    )


def get_ticket_type_service(
    ticket_type_repository: InMemoryTicketTypeRepository = Depends(get_ticket_type_repository),
) -> TicketTypeService:
    return TicketTypeService(
        repository=ticket_type_repository,
    )

