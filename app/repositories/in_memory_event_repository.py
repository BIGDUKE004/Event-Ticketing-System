from typing import List, Optional
from uuid import UUID

from app.models.event import Event
from app.repositories.event_repository import EventRepository


class InMemoryEventRepository(EventRepository):

    def __init__(self):
        self.__events: List[Event] = []

    def add(self, event: Event) -> Event:
        self.__events.append(event)
        return event

    def get(self, event_id: UUID) -> Optional[Event]:
        for event in self.__events:
            if event.id == event_id:
                return event
        return None

    def update(self, event_id: UUID, data: dict) -> Optional[Event]:
        event = self.get(event_id)
        if event is None:
            return None
        updated = event.model_copy(update=data)
        index = self.__events.index(event)
        self.__events[index] = updated
        return updated

    def get_all(self) -> List[Event]:
        return self.__events

    def delete(self, event_id: UUID) -> bool:
        event = self.get(event_id)
        if event is None:
            return False
        self.__events.remove(event)
        return True