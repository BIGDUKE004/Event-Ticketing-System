from fastapi import Depends
from app.repositories.event_repository import EventRepository
from app.repositories.in_memory_event_repository import InMemoryEventRepository

from app.services.event_service import EventService

_repository = InMemoryEventRepository()

def get_event_repository() -> EventRepository:
    return _repository

def get_event_service(
    repository: EventRepository = Depends(get_event_repository)
) -> EventService:
    return EventService(repository)