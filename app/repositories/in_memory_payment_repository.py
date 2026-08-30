from typing import List, Optional
from uuid import UUID

from app.models.payment import Payment
from app.repositories.payment_repository import PaymentRepository


class InMemoryPaymentRepository(PaymentRepository):

    def __init__(self):
        self.__payments: List[Payment] = []

    def add(self, payment: Payment) -> Payment:
        self.__payments.append(payment)
        return payment

    def get(self, payment_id: UUID) -> Optional[Payment]:
        for payment in self.__payments:
            if payment_id == payment_id:
                return payment
        return None

    def get_all(self) -> List[Payment]:
        return self.__payments



