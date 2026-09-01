from uuid import UUID

from sqlalchemy.orm import Session

from app.models.ticket_type import TicketType
from app.database_models.ticket_type import TicketTypeDB
from app.repositories.ticket_type_repository import TicketTypeRepository


class SQLTicketTypeRepository(TicketTypeRepository):

    def __init__(self, db: Session):
        self.db = db

    def create(self, ticket_type: TicketType) -> TicketType:

        db_ticket_type = TicketTypeDB(
            id=ticket_type.id,
            event_id=ticket_type.event_id,
            name=ticket_type.name,
            price=ticket_type.price,
            quantity=ticket_type.quantity,
            available_quantity=ticket_type.available_quantity,
            sold_out=ticket_type.sold_out
        )

        self.db.add(db_ticket_type)
        self.db.commit()
        self.db.refresh(db_ticket_type)

        return ticket_type

    def get_by_id(
        self,
        ticket_type_id: UUID
    ) -> TicketType | None:

        db_ticket_type = self.db.get(
            TicketTypeDB,
            ticket_type_id
        )

        if db_ticket_type is None:
            return None

        return TicketType(
            id=UUID(str(db_ticket_type.id)),
            event_id=db_ticket_type.event_id,
            name=db_ticket_type.name,
            price=db_ticket_type.price,
            quantity=db_ticket_type.quantity,
            available_quantity=db_ticket_type.available_quantity,
            sold_out=db_ticket_type.sold_out
        )

    def get_by_event_id(
        self,
        event_id: str
    ) -> list[TicketType]:

        db_ticket_types = (
            self.db.query(TicketTypeDB)
            .filter(TicketTypeDB.event_id == event_id)
            .all()
        )

        return [
            TicketType(
                id=UUID(str(ticket_type.id)),
                event_id=ticket_type.event_id,
                name=ticket_type.name,
                price=ticket_type.price,
                quantity=ticket_type.quantity,
                available_quantity=ticket_type.available_quantity,
                sold_out=ticket_type.sold_out
            )
            for ticket_type in db_ticket_types
        ]

    def update(self, ticket_type: TicketType) -> TicketType:

        db_ticket_type = self.db.get(
            TicketTypeDB.id
        )

        if db_ticket_type is None:
            return ticket_type

        db_ticket_type.event_id = ticket_type.event_id
        db_ticket_type.name = ticket_type.name
        db_ticket_type.price = ticket_type.price
        db_ticket_type.quantity = ticket_type.quantity
        db_ticket_type.available_quantity = ticket_type.available_quantity
        db_ticket_type.sold_out = ticket_type.sold_out

        self.db.commit()
        self.db.refresh(db_ticket_type)

        return ticket_type

    def delete(self, ticket_type_id: UUID) -> bool:

        db_ticket_type = self.db.get(
            TicketTypeDB,
            ticket_type_id
        )

        if db_ticket_type is None:
            return False

        self.db.delete(db_ticket_type)
        self.db.commit()

        return True