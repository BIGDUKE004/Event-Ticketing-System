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
from app.repositories.SQLUserRepository import SQLUserRepository
from app.repositories.SQLPaymentRepository import SQLPaymentRepository
from app.repositories.payment_repository import PaymentRepository
from app.services.payment_service import PaymentService
from app.repositories.SQLBookingRepository import SQLBookingRepository


def get_event_repository(
    db: Session = Depends(get_db)
) -> EventRepository:
    return SQLEventRepository(db)

def get_booking_repository(db: Session = Depends(get_db)) -> BookingRepository:
    return SQLBookingRepository(db)

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

def get_user_repository(db: Session = Depends(get_db)) -> SQLUserRepository:
    return SQLUserRepository(db)

def get_user_service(
       db: Session = Depends(get_db),  user_repository: UserRepository = Depends(get_user_repository)
) -> AuthService:
    repository = SQLUserRepository(db)
    return AuthService(repository)



def get_booking_service(
        db: Session = Depends(get_db)
) -> BookingService:
    repository = SQLBookingRepository(db)
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

