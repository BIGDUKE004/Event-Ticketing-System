from uuid import UUID

from models.ticket_type import TicketType


class TicketTypeService:

    def __init__(self, repository):
        self.repository = repository

    def create_ticket_type(self, ticket_type: TicketType) -> TicketType:
        return self.repository.create(ticket_type)

    def get_ticket_type(self, ticket_type_id: UUID) -> TicketType | None:
        return self.repository.get_by_id(ticket_type_id)

    def get_ticket_types_by_event(
        self,
        event_id: str
    ) -> list[TicketType]:
        return self.repository.get_by_event_id(event_id)

    def update_ticket_type(self, ticket_type: TicketType) -> TicketType | None:
        existing_ticket_type = self.repository.get_by_id(ticket_type.id)

        if existing_ticket_type is None:
            return None

        return self.repository.update(ticket_type)

    def delete_ticket_type(self, ticket_type_id: UUID) -> bool:
        return self.repository.delete(ticket_type_id)