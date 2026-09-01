from datetime import datetime, timezone
from uuid import UUID

from pydantic import Field

from app.models.payment import CreatePayment, PaymentResponse
from app.database_models.payment import Payment
from app.models.payment_status_enum import PaymentStatus
from app.repositories.booking_repository import BookingRepository
from app.repositories.payment_repository import PaymentRepository


class PaymentService:
    def __init__(self, repository: PaymentRepository, booking_repository: BookingRepository):
        self.__repository = repository
        self.__booking_repository = booking_repository

    def process_payment(self, payload: CreatePayment) -> PaymentResponse:
        booking = self.__booking_repository.get_booking_information(str(payload.booking_id))
        if booking.total_amount > payload.amount:
            raise ValueError("Insufficient funds")

        payment = Payment(
            booking_id=payload.booking_id,
            amount=payload.amount,
            payment_status=PaymentStatus.SUCCESSFUL
        )
        saved_payment = self.__repository.add(payment)
        return PaymentResponse.model_validate(saved_payment)

    def get_all_payments(self):
        return self.__repository.get_all()

    def get_booking_payment(self, booking_id: UUID):
        payments = self.get_all_payments()
        for payment in payments:
            if payment.booking_id == str(booking_id):
                return PaymentResponse.model_validate(payment)





