from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, status, HTTPException

from app.dependencies import get_event_service
from app.models.event import CreateEvent, UpdateEvent, EventResponse
from app.services.event_service import EventService

router = APIRouter(prefix="/events", tags=["Events"])

@router.post("/", response_model=EventResponse, status_code=status.HTTP_201_CREATED)
def create_event(
    payload: CreateEvent,
    user_id: UUID,
    service: EventService = Depends(get_event_service),
):
    try:
        return service.create_event(payload, user_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))



@router.get("/", response_model=List[EventResponse])
def get_all_event(service: EventService = Depends(get_event_service)):
    return service.get_all_event()

@router.get("/search", response_model=List[EventResponse])
def search_events(
        keyword: str,
        service: EventService = Depends(get_event_service)):
    return service.search_events(keyword)


@router.get("/{event_id}", response_model=EventResponse)
def find_event(
    event_id: UUID,
    service: EventService = Depends(get_event_service),
):
    try:
        return service.find_event(event_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/{event_id}/tickets_sold", response_model=int)
def get_total_tickets_sold(
    event_id: UUID,
    service: EventService = Depends(get_event_service),
):
    try:
        return service.get_total_tickets_sold(event_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/{event_id}/amount_made", response_model=float)
def get_total_amount_made(
    event_id: UUID,
    service: EventService = Depends(get_event_service),
):
    try:
        return service.get_total_amount_made(event_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.patch("/{event_id}", response_model=EventResponse)
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

