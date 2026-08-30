from abc import ABC, abstractmethod
from uuid import UUID

from app.models.ticket import Ticket


class TicketRepository(ABC):

    @abstractmethod
    def create(self, ticket: Ticket) -> Ticket:
        pass

    @abstractmethod
    def get_by_id(self, ticket_id: UUID) -> Ticket | None:
        pass

    @abstractmethod
    def get_by_booking_id(self, booking_id: str) -> list[Ticket]:
        pass

    @abstractmethod
    def update(self, ticket: Ticket) -> Ticket:
        pass

    @abstractmethod
    def delete(self, ticket_id: UUID) -> bool:
        pass