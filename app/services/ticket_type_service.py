from uuid import UUID

from app.models.ticket_type import TicketType, CreateTicketType, UpdateTicketType


class TicketTypeService:

    def __init__(self, repository):
        self.repository = repository

    def create_ticket_type(self, data: CreateTicketType) -> TicketType:

        ticket_type = TicketType(
            event_id=data.event_id,
            name=data.name,
            price=data.price,
            quantity=data.quantity,
            available_quantity=data.quantity,
            sold_out=False
        )
        return self.repository.create(ticket_type)

    def get_ticket_type(self, ticket_type_id: UUID) -> TicketType | None:
        return self.repository.get_by_id(ticket_type_id)

    def get_ticket_types_by_event(
        self,
        event_id: str
    ) -> list[TicketType]:
        return self.repository.get_by_event_id(event_id)

    def update_ticket_type(self, ticket_type: UpdateTicketType) -> TicketType | None:
        existing_ticket_type = self.repository.get_by_id(ticket_type.id)

        if existing_ticket_type is None:
            return None

        return self.repository.update(ticket_type)

    def delete_ticket_type(self, ticket_type_id: UUID) -> bool:
        return self.repository.delete(ticket_type_id)