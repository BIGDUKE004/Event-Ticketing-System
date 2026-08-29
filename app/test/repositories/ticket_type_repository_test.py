import uuid

from models.ticket_type import TicketType
from repositories.in_memory_ticket_type_repository import InMemoryTicketTypeRepository


def create_ticket_type(event_id="event-123", name="VIP"):
    return TicketType(
        event_id=event_id,
        name=name,
        price=50000,
        quantity=100,
        available_quantity=100,
        sold_out=False
    )


def test_create_ticket_type_works():
    repository = InMemoryTicketTypeRepository()
    ticket_type = create_ticket_type()

    result = repository.create(ticket_type)

    assert result == ticket_type
    assert result.id in repository.ticket_types


def test_get_ticket_type_by_id_is_working():
    repository = InMemoryTicketTypeRepository()
    ticket_type = create_ticket_type()

    repository.create(ticket_type)

    result = repository.get_by_id(ticket_type.id)

    assert result == ticket_type


def test_get_ticket_type_by_id_returns_none_when_not_found():
    repository = InMemoryTicketTypeRepository()

    result = repository.get_by_id(uuid.uuid4())

    assert result is None


def test_get_ticket_types_by_event_id():
    repository = InMemoryTicketTypeRepository()

    vip = create_ticket_type(event_id="event-123", name="VIP")
    regular = create_ticket_type(event_id="event-123", name="Regular")
    other = create_ticket_type(event_id="event-456", name="VIP")

    repository.create(vip)
    repository.create(regular)
    repository.create(other)

    result = repository.get_by_event_id("event-123")

    assert len(result) == 2
    assert vip in result
    assert regular in result
    assert other not in result



def test_update_ticket_type_works():
    repository = InMemoryTicketTypeRepository()
    ticket_type = create_ticket_type()

    repository.create(ticket_type)

    ticket_type.available_quantity = 50
    ticket_type.sold_out = False

    result = repository.update(ticket_type)

    assert result == ticket_type
    assert result.available_quantity == 50
    assert repository.get_by_id(ticket_type.id).available_quantity == 50


def test_delete_ticket_type():
    repository = InMemoryTicketTypeRepository()
    ticket_type = create_ticket_type()

    repository.create(ticket_type)

    result = repository.delete(ticket_type.id)

    assert result is True
    assert repository.get_by_id(ticket_type.id) is None


def test_delete_ticket_type_returns_false_when_not_found():
    repository = InMemoryTicketTypeRepository()

    result = repository.delete(uuid.uuid4())

    assert result is False