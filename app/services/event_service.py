from typing import List, Optional
from uuid import UUID

from app.models.event import CreateEvent, UpdateEvent, EventResponse
from app.database_models.event import Event as EventModel
from app.repositories.event_repository import EventRepository
from app.repositories.booking_repository import BookingRepository
from app.repositories.ticket_type_repository import TicketTypeRepository


class EventService:
    def __init__(self, repository: EventRepository, booking_repository: BookingRepository, ticket_type_repository: TicketTypeRepository):
        self.__repository = repository
        self.__booking_repository = booking_repository
        self.__ticket_type_repository = ticket_type_repository


    def create_event(self, payload: CreateEvent,user_id: UUID) -> EventModel:
        event = EventModel(name=payload.name, description=payload.description, location=payload.location, organizer_id=user_id)

        if len(payload.name.strip()) == 0:
            raise ValueError("Event name cannot be blank")

        return self.__repository.add(event)

    def update_event(self, event_id: UUID, payload: UpdateEvent) -> EventModel:
        data = payload.model_dump(exclude_unset=True)
        event = self.__repository.update(event_id, data)
        if event is None:
            raise ValueError("No such event found")
        return event

    def find_event(self, event_id: UUID) -> EventResponse:
        event : Optional[EventModel] = self.__repository.get(event_id)
        if event is None:
            raise ValueError("Event does not exist")

        ticket_types = self.__ticket_type_repository.get_by_event_id(
            str(event_id)
        )

        event_response = EventResponse.model_validate(event)
        event_response.ticket_types = ticket_types
        return event_response

    def get_all_event(self) -> List[EventResponse]:
        events : List[EventModel] = self.__repository.get_all()
        event_responses = []

        for event in events:

            ticket_types = self.__ticket_type_repository.get_by_event_id(
                str(event.id)
            )

            event_response = EventResponse.model_validate(event)
            event_response.ticket_types = ticket_types
            event_responses.append(event_response)
        return event_responses

    def delete_event(self, event_id: UUID) -> None:
        event = self.find_event(event_id)
        if event is None:
            raise ValueError("Event does not exist")
        self.__repository.delete(event_id)

    def search_events(self, keyword: str) -> List[EventModel]:
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
            if booking.event_id == str(event_id):
                number_of_tickets_sold += booking.quantity
        return number_of_tickets_sold

    def get_total_amount_made(self, event_id: UUID) -> float:
        bookings = self.__booking_repository.get_all_bookings()
        total_amount_made = 0.0
        for booking in bookings:
            if booking.event_id == str(event_id):
                total_amount_made += booking.total_amount
        return total_amount_made
