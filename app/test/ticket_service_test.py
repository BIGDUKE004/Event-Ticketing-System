import uuid

import pytest

from models.ticket import Ticket, CreateTicket
from models.ticket_type import TicketType
from repositories.in_memory_ticket_repository import InMemoryTicketRepository
from repositories.in_memory_ticket_type_repository import InMemoryTicketTypeRepository
from services.ticket_service import TicketService


def create_service():
    ticket_repository = InMemoryTicketRepository()
    ticket_type_repository = InMemoryTicketTypeRepository()

    service = TicketService(
        ticket_repository=ticket_repository,
        ticket_type_repository=ticket_type_repository
    )

    return service, ticket_repository, ticket_type_repository


def create_ticket_type(available_quantity=100):
    return TicketType(
        event_id="event-123",
        name="VIP",
        price=50000,
        quantity=100,
        available_quantity=available_quantity,
        sold_out=available_quantity == 0
    )


def create_ticket_request(
    ticket_type_id,
    booking_id="booking-123",
    ticket_code="TICKET-001"
):
    return CreateTicket(
        ticket_type_id=str(ticket_type_id),
        booking_id=booking_id,
        ticket_code=ticket_code
    )


def create_ticket(
    ticket_type_id,
    booking_id="booking-123",
    ticket_code="TICKET-001"
):
    return Ticket(
        ticket_type_id=str(ticket_type_id),
        booking_id=booking_id,
        ticket_code=ticket_code
    )


def test_create_ticket_works():
    service, ticket_repository, ticket_type_repository = create_service()

    ticket_type = create_ticket_type()

    ticket_type_repository.create(ticket_type)

    ticket_request = create_ticket_request(ticket_type.id)

    result = service.create_ticket(ticket_request)

    assert result is not None
    assert result.booking_id == ticket_request.booking_id
    assert result.ticket_type_id == ticket_request.ticket_type_id
    assert result.ticket_code == ticket_request.ticket_code

    stored_ticket = ticket_repository.get_by_id(result.id)

    assert stored_ticket == result


def test_create_ticket_decreases_available_quantity():
    service, _, ticket_type_repository = create_service()

    ticket_type = create_ticket_type(
        available_quantity=100
    )

    ticket_type_repository.create(ticket_type)

    ticket_request = create_ticket_request(ticket_type.id)

    service.create_ticket(ticket_request)

    updated_ticket_type = ticket_type_repository.get_by_id(
        ticket_type.id
    )

    assert updated_ticket_type.available_quantity == 99


def test_create_ticket_sets_sold_out_when_ticket_quantity_reaches_zero():
    service, _, ticket_type_repository = create_service()

    ticket_type = create_ticket_type(
        available_quantity=1
    )

    ticket_type_repository.create(ticket_type)

    ticket_request = create_ticket_request(ticket_type.id)

    service.create_ticket(ticket_request)

    updated_ticket_type = ticket_type_repository.get_by_id(
        ticket_type.id
    )

    assert updated_ticket_type.available_quantity == 0
    assert updated_ticket_type.sold_out is True


def test_create_ticket_raises_error_when_ticket_type_not_found():
    service, _, _ = create_service()

    ticket_request = create_ticket_request(uuid.uuid4())

    with pytest.raises(
        ValueError,
        match="Ticket type not found"
    ):
        service.create_ticket(ticket_request)


def test_create_ticket_raises_error_when_ticket_type_is_sold_out():
    service, _, ticket_type_repository = create_service()

    ticket_type = create_ticket_type(
        available_quantity=0
    )

    ticket_type_repository.create(ticket_type)

    ticket_request = create_ticket_request(ticket_type.id)

    with pytest.raises(
        ValueError,
        match="Ticket type is sold out"
    ):
        service.create_ticket(ticket_request)


def test_get_ticket_works():
    service, ticket_repository, _ = create_service()

    ticket = create_ticket(
        uuid.uuid4()
    )

    ticket_repository.create(ticket)

    result = service.get_ticket(ticket.id)

    assert result == ticket


def test_get_ticket_returns_none_when_not_found():
    service, _, _ = create_service()

    result = service.get_ticket(uuid.uuid4())

    assert result is None


def test_get_tickets_by_booking_works():
    service, ticket_repository, _ = create_service()

    ticket_type_id = uuid.uuid4()

    ticket1 = create_ticket(
        ticket_type_id,
        booking_id="booking-123",
        ticket_code="TICKET-001"
    )

    ticket2 = create_ticket(
        ticket_type_id,
        booking_id="booking-123",
        ticket_code="TICKET-002"
    )

    ticket3 = create_ticket(
        ticket_type_id,
        booking_id="booking-456",
        ticket_code="TICKET-003"
    )

    ticket_repository.create(ticket1)
    ticket_repository.create(ticket2)
    ticket_repository.create(ticket3)

    result = service.get_tickets_by_booking(
        "booking-123"
    )

    assert len(result) == 2
    assert ticket1 in result
    assert ticket2 in result
    assert ticket3 not in result


def test_delete_ticket_is_working():
    service, ticket_repository, _ = create_service()

    ticket = create_ticket(
        uuid.uuid4()
    )

    ticket_repository.create(ticket)

    result = service.delete_ticket(ticket.id)

    assert result is True
    assert ticket_repository.get_by_id(ticket.id) is None


def test_delete_ticket_returns_false_when_not_found():
    service, _, _ = create_service()

    result = service.delete_ticket(uuid.uuid4())

    assert result is False