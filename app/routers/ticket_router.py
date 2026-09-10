from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import get_ticket_service
from app.models.ticket import Ticket, CreateTicket
from app.services.ticket_service import TicketService


router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)


@router.post("/", response_model=Ticket)
def create_ticket(
    ticket: CreateTicket,
    service: TicketService = Depends(get_ticket_service)
):
    try:
        return service.create_ticket(ticket)

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.get(
    "/{ticket_id}",
    response_model=Ticket
)
def get_ticket(
    ticket_id: UUID,
    service: TicketService = Depends(get_ticket_service)
):
    ticket = service.get_ticket(ticket_id)

    if ticket is None:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return ticket


@router.get(
    "/booking/{booking_id}",
    response_model=list[Ticket]
)
def get_tickets_by_booking(
    booking_id: str,
    service: TicketService = Depends(get_ticket_service)
):
    return service.get_tickets_by_booking(booking_id)


@router.delete("/{ticket_id}")
def delete_ticket(
    ticket_id: UUID,
    service: TicketService = Depends(get_ticket_service)
):
    result = service.delete_ticket(ticket_id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return {
        "message": "Ticket deleted successfully"
    }