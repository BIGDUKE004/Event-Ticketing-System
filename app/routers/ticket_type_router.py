from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import get_ticket_type_service
from app.models.ticket_type import TicketType, CreateTicketType, UpdateTicketType
from app.services.ticket_type_service import TicketTypeService


router = APIRouter(
    prefix="/ticket-types",
    tags=["Ticket Types"]
)


@router.post("/", response_model=TicketType)
def create_ticket_type(ticket_type: CreateTicketType,
    service: TicketTypeService = Depends(get_ticket_type_service)   ):
    return service.create_ticket_type(ticket_type)


@router.get(
    "/{ticket_type_id}",
    response_model=TicketType)

def get_ticket_type(ticket_type_id: UUID,
    service: TicketTypeService = Depends(get_ticket_type_service)
):
    ticket_type = service.get_ticket_type(ticket_type_id)

    if ticket_type is None:
        raise HTTPException(
            status_code=404,
            detail="Ticket type not found"
        )

    return ticket_type


@router.get("/event/{event_id}",
    response_model=list[TicketType]
)
def get_ticket_types_by_event(event_id: str,
service: TicketTypeService = Depends(get_ticket_type_service)
):
    return service.get_ticket_types_by_event(event_id)


@router.put( "/{ticket_type_id}",
response_model=TicketType
)
def update_ticket_type(
    ticket_type_id: UUID,
    ticket_type: UpdateTicketType,
    service: TicketTypeService = Depends(get_ticket_type_service)
):
    if ticket_type.id != ticket_type_id:
        raise HTTPException(
            status_code=400,
            detail="Ticket type ID does not match URL ID"
        )

    updated_ticket_type = service.update_ticket_type(ticket_type)

    if updated_ticket_type is None:
        raise HTTPException(
            status_code=404,
            detail="Ticket type not found"
        )

    return updated_ticket_type


@router.delete("/{ticket_type_id}")
def delete_ticket_type(
    ticket_type_id: UUID,
    service: TicketTypeService = Depends(get_ticket_type_service)
):
    result = service.delete_ticket_type(ticket_type_id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Ticket type not found"
        )

    return { "message": "Ticket type deleted successfully"
    }