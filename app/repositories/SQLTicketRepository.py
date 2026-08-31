from uuid import UUID

from sqlalchemy.orm import Session

from app.models.ticket import Ticket
from app.database_models.ticket import TicketDB
from app.repositories.ticket_repository import TicketRepository


class SQLTicketRepository(TicketRepository):

    def __init__(self, db: Session):
        self.db = db

    def create(self, ticket: Ticket) -> Ticket:

        db_ticket = TicketDB(
            id=ticket.id,
            booking_id=ticket.booking_id,
            ticket_type_id=ticket.ticket_type_id,
            ticket_code=ticket.ticket_code,
            created_at=ticket.created_at
        )

        self.db.add(db_ticket)
        self.db.commit()
        self.db.refresh(db_ticket)

        return ticket

    def get_by_id(
        self,
        ticket_id: UUID
    ) -> Ticket | None:

        db_ticket = self.db.get(
            TicketDB,
            ticket_id
        )

        if db_ticket is None:
            return None

        return Ticket(
            id=UUID(str(db_ticket.id)),
            booking_id=db_ticket.booking_id,
            ticket_type_id=str(db_ticket.ticket_type_id),
            ticket_code=db_ticket.ticket_code,
            created_at=db_ticket.created_at
        )

    def get_by_booking_id(
        self,
        booking_id: str
    ) -> list[Ticket]:

        db_tickets = (
            self.db.query(TicketDB)
            .filter(TicketDB.booking_id == booking_id)
            .all()
        )

        return [
            Ticket(
                id=UUID(str(ticket.id)),
                booking_id=ticket.booking_id,
                ticket_type_id=str(ticket.ticket_type_id),
                ticket_code=ticket.ticket_code,
                created_at=ticket.created_at
            )
            for ticket in db_tickets
        ]

    def update(self, ticket: Ticket) -> Ticket:

        db_ticket = self.db.get(
            TicketDB,
            ticket.id
        )

        if db_ticket is None:
            return ticket

        db_ticket.booking_id = ticket.booking_id
        db_ticket.ticket_type_id = ticket.ticket_type_id
        db_ticket.ticket_code = ticket.ticket_code
        db_ticket.created_at = ticket.created_at

        self.db.commit()
        self.db.refresh(db_ticket)

        return ticket

    def delete(self, ticket_id: UUID) -> bool:

        db_ticket = self.db.get(
            TicketDB,
            ticket_id
        )

        if db_ticket is None:
            return False

        self.db.delete(db_ticket)
        self.db.commit()

        return True