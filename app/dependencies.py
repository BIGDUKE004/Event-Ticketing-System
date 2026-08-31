from fastapi import Depends
from sqlalchemy.orm import Session

from app.repositories.event_repository import EventRepository
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService
from app.services.event_service import EventService

from app.repositories.booking_repository import BookingRepository
from app.services.booking_service import BookingService
from app.repositories.SQLEventRepository import SQLEventRepository
from app.repositories.SQLTicketRepository import SQLTicketRepository
from app.services.ticket_service import TicketService
from app.repositories.SQLTicketTypeRepository import SQLTicketTypeRepository
from app.services.ticket_type_service import TicketTypeService
from app.database import get_db
from app.repositories.in_memory_booking_repository import InMemoryBookingRepository
from app.repositories.SQLUserRepository import SQLUserRepository


_booking_repository = InMemoryBookingRepository()


def get_event_repository(
    db: Session = Depends(get_db)
) -> EventRepository:
    return SQLEventRepository(db)

def get_booking_repository() -> BookingRepository:
    return _booking_repository

def get_event_service(
    db: Session = Depends(get_db),
    booking_repository: BookingRepository = Depends(get_booking_repository)
) -> EventService:
    repository = SQLEventRepository(db)
    return EventService(repository, booking_repository)



def get_user_repository(db: Session = Depends(get_db)) -> SQLUserRepository:
    return SQLUserRepository(db)

def get_user_service(
       db: Session = Depends(get_db),  user_repository: UserRepository = Depends(get_user_repository)
) -> AuthService:
    repository = SQLUserRepository(db)
    return AuthService(repository)



def get_booking_service(
        repository: BookingRepository = Depends(get_booking_repository)
) -> BookingService:
    return BookingService(repository)

def get_ticket_repository(
    db: Session = Depends(get_db)
) -> SQLTicketRepository:

    return SQLTicketRepository(db)

def get_ticket_type_repository(
    db: Session = Depends(get_db)
) -> SQLTicketTypeRepository:

    return SQLTicketTypeRepository(db)


def get_ticket_service(
    ticket_repository: SQLTicketRepository = Depends(
        get_ticket_repository
    ),
    ticket_type_repository: SQLTicketTypeRepository = Depends(
        get_ticket_type_repository
    ),
) -> TicketService:

    return TicketService(
        ticket_repository=ticket_repository,
        ticket_type_repository=ticket_type_repository,
    )


def get_ticket_type_service(
    ticket_type_repository: SQLTicketTypeRepository = Depends(
        get_ticket_type_repository
    ),
) -> TicketTypeService:

    return TicketTypeService(
        repository=ticket_type_repository
    )

