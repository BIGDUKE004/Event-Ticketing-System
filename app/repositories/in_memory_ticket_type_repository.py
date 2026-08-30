from uuid import UUID

from app.models.ticket_type import TicketType
from app.repositories.ticket_type_repository import TicketTypeRepository


class InMemoryTicketTypeRepository(TicketTypeRepository):

    def __init__(self):
        self.ticket_types: dict[UUID, TicketType] = {}

    def create(self, ticket_type: TicketType) -> TicketType:
        self.ticket_types[ticket_type.id] = ticket_type
        return ticket_type

    def get_by_id(self, ticket_type_id: UUID) -> TicketType | None:
        return self.ticket_types.get(ticket_type_id)

    def get_by_event_id(self, event_id: str) -> list[TicketType]:
        return [
            ticket_type
            for ticket_type in self.ticket_types.values()
            if ticket_type.event_id == event_id
        ]

    def update(self, ticket_type: TicketType) -> TicketType:
        self.ticket_types[ticket_type.id] = ticket_type
        return ticket_type

    def delete(self, ticket_type_id: UUID) -> bool:
        if ticket_type_id in self.ticket_types:
            del self.ticket_types[ticket_type_id]
            return True

        return False