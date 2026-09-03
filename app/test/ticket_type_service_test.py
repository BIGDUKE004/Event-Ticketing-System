import uuid

from models.ticket_type import (
    TicketType,
    CreateTicketType,
    UpdateTicketType
)

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


def create_ticket_type_data(
    event_id="event-123",
    name="VIP",
    price=50000,
    quantity=100
):
    return CreateTicketType(
        event_id=event_id,
        name=name,
        price=price,
        quantity=quantity
    )


def create_service():
    repository = InMemoryTicketTypeRepository()
    service = TicketTypeService(repository)

    return service, repository


def test_create_ticket_type():
    service, repository = create_service()

    data = create_ticket_type_data()

    result = service.create_ticket_type(data)

    assert result.event_id == data.event_id
    assert result.name == data.name
    assert result.price == data.price
    assert result.quantity == data.quantity
    assert result.available_quantity == data.quantity
    assert result.sold_out is False
    assert result.id is not None
    assert isinstance(result.id, uuid.UUID)

    assert repository.get_by_id(result.id) == result


def test_get_ticket_type():
    service, repository = create_service()

    ticket_type = create_ticket_type()

    repository.create(ticket_type)

    result = service.get_ticket_type(ticket_type.id)

    assert result == ticket_type


def test_get_ticket_type_returns_none_when_not_found():
    service, _ = create_service()

    ticket_type_id = uuid.uuid4()

    result = service.get_ticket_type(ticket_type_id)

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

    update_data = UpdateTicketType(
        name="Odogwu",
        price=75000
    )

    result = service.update_ticket_type(
        ticket_type.id,
        update_data
    )

    assert result is not None
    assert result.id == ticket_type.id
    assert result.name == "Odogwu"
    assert result.price == 75000
    assert result.event_id == ticket_type.event_id
    assert result.quantity == ticket_type.quantity
    assert result.available_quantity == ticket_type.available_quantity
    assert result.sold_out == ticket_type.sold_out


def test_update_non_existing_ticket_type_returns_none():
    service, _ = create_service()

    ticket_type_id = uuid.uuid4()

    update_data = UpdateTicketType(
        name="Odogwu",
        price=75000
    )

    result = service.update_ticket_type(
        ticket_type_id,
        update_data
    )

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

    ticket_type_id = uuid.uuid4()

    result = service.delete_ticket_type(ticket_type_id)

    assert result is False

