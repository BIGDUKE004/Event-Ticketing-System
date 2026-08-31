from fastapi import Depends
from sqlalchemy.orm import Session

from app.repositories.event_repository import EventRepository
from app.repositories.payment_repository import PaymentRepository
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService
from app.services.event_service import EventService

from app.repositories.booking_repository import BookingRepository
from app.services.booking_service import BookingService
from app.repositories.SQLEventRepository import SQLEventRepository
from app.repositories.in_memory_ticket_repository import InMemoryTicketRepository
from app.services.ticket_service import TicketService
from app.repositories.in_memory_ticket_type_repository import InMemoryTicketTypeRepository
from app.services.ticket_type_service import TicketTypeService
from app.database import get_db
from app.repositories.in_memory_booking_repository import InMemoryBookingRepository
from app.repositories.SQLPaymentRepository import SQLPaymentRepository
from app.repositories.payment_repository import PaymentRepository
from app.services.payment_service import PaymentService

_ticket_repository = InMemoryTicketRepository()
_ticket_type_repository = InMemoryTicketTypeRepository()
_booking_repository = InMemoryBookingRepository()

def get_event_repository(
    db: Session = Depends(get_db)
) -> EventRepository:
    return SQLEventRepository(db)

def get_booking_repository() -> BookingRepository:
    return _booking_repository

def get_event_service(
    event_repository: EventRepository = Depends(get_event_repository),
    booking_repository: BookingRepository = Depends(get_booking_repository)
) -> EventService:
    return EventService(event_repository, booking_repository)

def get_payment_repository(
    db: Session = Depends(get_db)
) -> PaymentRepository:
    return SQLPaymentRepository(db)

def get_payment_service(
    payment_repository: PaymentRepository = Depends(get_payment_repository),
    booking_repository: BookingRepository = Depends(get_booking_repository)
) -> PaymentService:
    return PaymentService(payment_repository, booking_repository)

def get_user_repository() -> UserRepository:
    return _repository

def get_user_service(
        repository: UserRepository = Depends(get_user_repository)
) -> AuthService:
    return AuthService(repository)



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

