from datetime import datetime, timezone
from uuid import UUID

from pydantic import Field

from models.payment import Payment
from models.payment_status_enum import PaymentStatus
from repositories import booking_repository
from repositories.booking_repository import BookingRepository
from repositories.payment_repository import PaymentRepository


class PaymentService:
    def __init__(self, repository: PaymentRepository, booking_repository: BookingRepository):
        self.__repository = repository
        self.__booking_repository = booking_repository

    def process_payment(self, booking_id: UUID, amount_paid: float):
        booking = self.__booking_repository.get_booking_information(booking_id)
        if booking.total_amount > amount_paid:
            raise ValueError("Insufficient funds")

        payment = Payment(
            booking_id=booking_id,
            amount=amount_paid,
            payment_status=PaymentStatus.SUCCESSFUL,
        )
        self.__repository.add(payment)
        return "payment successful"

