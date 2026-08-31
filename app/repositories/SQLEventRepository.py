from typing import Optional, List
from uuid import UUID

from sqlalchemy.orm import Session

from app.database_models.event import Event as EventModel
from app.repositories.event_repository import EventRepository


class SQLEventRepository(EventRepository):

    def __init__(self, db: Session):
        self.db = db

    def add(self, event: EventModel):
        self.db.add(event)
        self.db.commit()
        self.db.refresh(event)
        return event

    def get(self, event_id: UUID) -> Optional[EventModel]:
        return self.db.query(EventModel).filter(EventModel.id == str(event_id)).first()

    def update(self, event_id: UUID, data: dict) -> Optional[EventModel]:
        event = self.get(event_id)
        if event is None:
            return None

        for key, value in data.items():
            setattr(event, key, value)

        self.db.commit()
        self.db.refresh(event)
        return event

    def get_all(self) :
        return self.db.query(EventModel).all()

    def delete(self, event_id: UUID) -> bool:
        event = self.get(event_id)
        if event is None:
            return False
        self.db.delete(event)
        self.db.commit()
        return True