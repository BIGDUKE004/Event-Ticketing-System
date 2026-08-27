from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID

from app.models.payment import Payment


class PaymentRepository(ABC):

    @abstractmethod
    def add(self, payment: Payment) -> Payment:
        pass

    @abstractmethod
    def get(self, payment_id: UUID) -> Optional[Payment]:
        pass

    @abstractmethod
    def get_all(self) -> List[Payment]:
        pass