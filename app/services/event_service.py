from typing import List
from uuid import UUID

from app.models.event import Event, CreateEvent, UpdateEvent
from app.repositories.event_repository import EventRepository
from app.repositories.booking_repository import BookingRepository


class EventService:
    def __init__(self, repository: EventRepository, booking_repository: BookingRepository):
        self.__repository = repository
        self.__booking_repository = booking_repository

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

    def get_total_tickets_sold(self, event_id: UUID) -> int:
        bookings = self.__booking_repository.get_all_bookings()
        number_of_tickets_sold = 0
        for booking in bookings:
            if booking.event_id == event_id:
                number_of_tickets_sold += booking.quantity
        return number_of_tickets_sold

    def get_total_amount_made(self, event_id: UUID) -> float:
        bookings = self.__booking_repository.get_all_bookings()
        total_amount_made = 0.0
        for booking in bookings:
            if booking.event_id == event_id:
                total_amount_made += booking.total_amount
        return total_amount_made
