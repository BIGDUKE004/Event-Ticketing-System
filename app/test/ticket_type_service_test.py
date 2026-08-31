import uuid

import pytest

from models.ticket_type import TicketType
from repositories.in_memory_ticket_type_repository import (
    InMemoryTicketTypeRepository
)
from services.ticket_type_service import TicketTypeService


def create_ticket_type(
    event_id="event-123",
    name="VIP",
    price=50000,
    quantity=100
):
    return TicketType(
        event_id=event_id,
        name=name,
        price=price,
        quantity=quantity,
        available_quantity=quantity,
        sold_out=False
    )


def create_service():
    repository = InMemoryTicketTypeRepository()
    service = TicketTypeService(repository)

    return service, repository


def test_create_ticket_type():
    service, repository = create_service()

    ticket_type = create_ticket_type()

    result = service.create_ticket_type(ticket_type)

    assert result == ticket_type
    assert repository.get_by_id(ticket_type.id) == ticket_type


def test_get_ticket_type():
    service, repository = create_service()

    ticket_type = create_ticket_type()

    repository.create(ticket_type)

    result = service.get_ticket_type(ticket_type.id)

    assert result == ticket_type


def test_get_ticket_type_returns_none_when_not_found():
    service, _ = create_service()

    result = service.get_ticket_type(uuid.uuid4())

    assert result is None


def test_get_ticket_types_by_event():
    service, repository = create_service()

    biggest_bird = create_ticket_type(
        event_id="event-123",
        name="Biggest bird"
    )

    regular = create_ticket_type(
        event_id="event-123",
        name="Regular"
    )

    early_bird = create_ticket_type(
        event_id="event-456",
        name="Early bird"
    )

    repository.create(biggest_bird)
    repository.create(regular)
    repository.create(early_bird)

    result = service.get_ticket_types_by_event("event-123")

    assert len(result) == 2
    assert biggest_bird in result
    assert regular in result
    assert early_bird not in result


def test_update_ticket_type():
    service, repository = create_service()

    ticket_type = create_ticket_type()

    repository.create(ticket_type)

    updated_ticket_type = TicketType(
        id=ticket_type.id,
        event_id=ticket_type.event_id,
        name="Odogwu",
        price=75000,
        quantity=ticket_type.quantity,
        available_quantity=ticket_type.available_quantity,
        sold_out=ticket_type.sold_out
    )

    result = service.update_ticket_type(updated_ticket_type)

    assert result == updated_ticket_type
    assert result.name == "Odogwu"
    assert result.price == 75000


def test_update_non_existing_ticket_type_returns_none():
    service, _ = create_service()

    ticket_type = create_ticket_type()

    result = service.update_ticket_type(ticket_type)

    assert result is None


def test_delete_ticket_type():
    service, repository = create_service()

    ticket_type = create_ticket_type()

    repository.create(ticket_type)

    result = service.delete_ticket_type(ticket_type.id)

    assert result is True
    assert repository.get_by_id(ticket_type.id) is None


def test_delete_non_existing_ticket_type():
    service, _ = create_service()

    result = service.delete_ticket_type(uuid.uuid4())

    assert result is False