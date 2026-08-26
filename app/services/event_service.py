from typing import List
from uuid import UUID

from app.models.event import Event, CreateEvent, UpdateEvent
from app.repositories.event_repository import EventRepository


class EventService:
    def __init__(self, repository: EventRepository):
        self.__repository = repository

    def create_event(self, payload: CreateEvent,organizer_id: str) -> Event:
        event = Event(name=payload.name, description=payload.description, location=payload.location, organizer_id=organizer_id)
        if len(payload.name) == 0:
            raise ValueError("Event name cannot be empty")
        if len(payload.name.strip()) == 0:
            raise ValueError("Event name cannot be blank")

        return self.__repository.add(event)

    def update_event(self, event_id: UUID, payload: UpdateEvent) -> Event:
        data = payload.model_dump(exclude_unset=True)
        event = self.__repository.update(event_id, data)
        if event is None:
            raise ValueError("No such event found")
        return event

    def find_event(self, event_id: UUID) -> Event:
        event = self.__repository.get(event_id)
        if event is None:
            raise ValueError("Event does not exist")
        return event

    def get_all_event(self) -> List[Event]:
        return self.__repository.get_all()

    def delete_event(self, event_id: UUID) -> None:
        event = self.find_event(event_id)
        if event is None:
            raise ValueError("Event does not exist")
        self.__repository.delete(event_id)

    def search_events(self, keyword: str) -> List[Event]:
        events = self.get_all_event()
        found_events = []
        for event in events:
            if keyword.lower() in event.name.lower() or keyword.lower() in event.description.lower():
                found_events.append(event)
        return found_events


