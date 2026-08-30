from uuid import UUID

from app.models.ticket import Ticket
from app.repositories.ticket_repository import TicketRepository


class InMemoryTicketRepository(TicketRepository):

    def __init__(self):
        self.tickets: dict[UUID, Ticket] = {}

    def create(self, ticket: Ticket) -> Ticket:
        self.tickets[ticket.id] = ticket
        return ticket

    def get_by_id(self, ticket_id: UUID) -> Ticket | None:
        return self.tickets.get(ticket_id)

    def get_by_booking_id(self, booking_id: str) -> list[Ticket]:
        return [
            ticket
            for ticket in self.tickets.values()
            if ticket.booking_id == booking_id
        ]

    def update(self, ticket: Ticket) -> Ticket:
        self.tickets[ticket.id] = ticket
        return ticket

    def delete(self, ticket_id: UUID) -> bool:
        if ticket_id not in self.tickets:
            return False

        del self.tickets[ticket_id]
        return True