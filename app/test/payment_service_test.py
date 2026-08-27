
import uuid

import pytest

from models import booking_status
from models.booking import Booking
from repositories import booking_repository
from repositories.in_memory_booking_repository import InMemoryBookingRepository
from repositories.in_memory_payment_repository import InMemoryPaymentRepository
from services.payment_service import PaymentService


@pytest.fixture
def booking_repository():
    return InMemoryBookingRepository()

@pytest.fixture
def payment_service(booking_repository):
     return PaymentService(InMemoryPaymentRepository(),
                           booking_repository)


def test_I_pay_exactly_amount_to_be_paid(payment_service, booking_repository):
    booking = Booking(

        user_id="user123",
        event_id="event123",
        ticket_type="VIP",
        bookings=[],
        quantity=1,
        total_amount=10000.0
    )

    booking_repository.save_booking(booking)

    payment = payment_service.process_payment(booking.id, 10000.0)
    assert payment == "payment successful"

