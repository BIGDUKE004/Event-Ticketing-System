from uuid import UUID

from app.models.ticket import Ticket, CreateTicket


class TicketService:

    def __init__(self, ticket_repository, ticket_type_repository):
        self.ticket_repository = ticket_repository
        self.ticket_type_repository = ticket_type_repository

    def create_ticket(self, ticket: CreateTicket) -> Ticket:
        try:
            ticket_type_id = UUID(ticket.ticket_type_id)
        except ValueError:
            raise ValueError("Invalid ticket type ID")

        ticket_type = self.ticket_type_repository.get_by_id(ticket_type_id)

        if ticket_type is None:
            raise ValueError("Ticket type not found")

        if ticket_type.available_quantity <= 0:
            raise ValueError("Ticket type is sold out")

        ticket_type.available_quantity -= 1

        if ticket_type.available_quantity == 0:
            ticket_type.sold_out = True

        self.ticket_type_repository.update(ticket_type)

        new_ticket = Ticket(
            booking_id=ticket.booking_id,
            ticket_type_id=ticket.ticket_type_id,
            ticket_code=ticket.ticket_code
        )

        return self.ticket_repository.create(new_ticket)

    def get_ticket(self, ticket_id: UUID) -> Ticket | None:
        return self.ticket_repository.get_by_id(ticket_id)

    def get_tickets_by_booking(
        self,
        booking_id: str
    ) -> list[Ticket]:
        return self.ticket_repository.get_by_booking_id(booking_id)

    def delete_ticket(self, ticket_id: UUID) -> bool:
        return self.ticket_repository.delete(ticket_id)