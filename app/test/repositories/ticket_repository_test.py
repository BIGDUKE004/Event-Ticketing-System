import uuid

from models.ticket import Ticket
from repositories.in_memory_ticket_repository import (InMemoryTicketRepository)


def create_ticket(
    booking_id="booking-123",
    ticket_type_id="ticket-type-123",
    ticket_code="TICKET-001"
):
    return Ticket(
        id=uuid.uuid4(),
        booking_id=booking_id,
        ticket_type_id=ticket_type_id,
        ticket_code=ticket_code
    )


def test_create_ticket_works():
    repository = InMemoryTicketRepository()

    ticket = create_ticket()
    result = repository.create(ticket)

    assert result == ticket


def test_get_ticket_by_id():
    repository = InMemoryTicketRepository()

    ticket = create_ticket()
    repository.create(ticket)
    result = repository.get_by_id(ticket.id)

    assert result == ticket


def test_get_ticket_by_id_returns_none_when_not_found():
    repository = InMemoryTicketRepository()

    ticket_id = uuid.uuid4()
    result = repository.get_by_id(ticket_id)

    assert result is None


def test_get_tickets_by_booking_id_works():
    repository = InMemoryTicketRepository()

    ticket1 = create_ticket(
        booking_id="booking-123",
        ticket_code="TICKET-001"
    )

    ticket2 = create_ticket(
        booking_id="booking-123",
        ticket_code="TICKET-002"
    )

    ticket3 = create_ticket(
        booking_id="booking-456",
        ticket_code="TICKET-003"
    )

    repository.create(ticket1)
    repository.create(ticket2)
    repository.create(ticket3)

    result = repository.get_by_booking_id("booking-123")

    assert len(result) == 2
    assert ticket1 in result
    assert ticket2 in result
    assert ticket3 not in result


def test_get_tickets_by_booking_id_returns_empty_list_when_not_found():
    repository = InMemoryTicketRepository()

    result = repository.get_by_booking_id("booking-999")

    assert result == []


def test_that_update_ticket_iz_working():
    repository = InMemoryTicketRepository()

    ticket = create_ticket()

    repository.create(ticket)

    ticket.ticket_code = "TICKET-UPDATED"

    result = repository.update(ticket)

    assert result == ticket

    updated_ticket = repository.get_by_id(ticket.id)

    assert updated_ticket.ticket_code == "TICKET-UPDATED"


def test_that_delete_ticket_works():
    repository = InMemoryTicketRepository()

    ticket = create_ticket()

    repository.create(ticket)

    result = repository.delete(ticket.id)

    assert result is True
    assert repository.get_by_id(ticket.id) is None


def test_delete_ticket_returns_false_when_not_found():
    repository = InMemoryTicketRepository()

    ticket_id = uuid.uuid4()

    result = repository.delete(ticket_id)

    assert result is False