from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, status, HTTPException

from app.dependencies import get_event_service
from app.models.event import Event, CreateEvent, UpdateEvent
from app.services.event_service import EventService

router = APIRouter(prefix="/events", tags=["Events"])

@router.post("/", response_model=Event, status_code=status.HTTP_201_CREATED)
def create_event(
    payload: CreateEvent,
    organizer_id: str,
    service: EventService = Depends(get_event_service),
):
    return service.create_event(payload, organizer_id)


@router.get("/", response_model=List[Event])
def get_all_event(service: EventService = Depends(get_event_service)):
    return service.get_all_event()

@router.get("/search", response_model=List[Event])
def search_events(
        keyword: str,
        service: EventService = Depends(get_event_service)):
    return service.search_events(keyword)


@router.get("/{event_id}", response_model=Event)
def find_event(
    event_id: UUID,
    service: EventService = Depends(get_event_service),
):
    try:
        return service.find_event(event_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{event_id}", response_model=Event)
def update_event(
    event_id: UUID,
    payload: UpdateEvent,
    service: EventService = Depends(get_event_service),
):
    try:
        return service.update_event(event_id, payload)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_event(
    event_id: UUID,
    service: EventService = Depends(get_event_service),
):
    try:
        service.delete_event(event_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

