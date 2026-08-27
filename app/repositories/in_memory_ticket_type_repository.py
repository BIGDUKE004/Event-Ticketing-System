from abc import ABC, abstractmethod
from uuid import UUID

from models.ticket_type import TicketType


class TicketTypeRepository(ABC):

    @abstractmethod
    def create(self, ticket_type: TicketType) -> TicketType:
        pass

    @abstractmethod
    def get_by_id(self, ticket_type_id: UUID) -> TicketType | None:
        pass

    @abstractmethod
    def get_by_event_id(self, event_id: str) -> list[TicketType]:
        pass

    @abstractmethod
    def update(self, ticket_type: TicketType) -> TicketType:
        pass

    @abstractmethod
    def delete(self, ticket_type_id: UUID) -> bool:
        pass