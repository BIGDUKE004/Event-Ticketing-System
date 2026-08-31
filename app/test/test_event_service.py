import unittest
import unittest.mock
import uuid
from datetime import datetime, timezone


import pytest
from app.models.event import CreateEvent, UpdateEvent
from app.repositories.SQLEventRepository import SQLEventRepository
from app.services.event_service import EventService

@pytest.fixture
def event_service():
     return EventService(InMemoryEventRepository())


def test_create_event_returns_event_details(event_service):

    event = event_service.create_event(CreateEvent(name="worship concert", description="worship in spirit and truth", location="Yaba, lagos", organizer_id="123"), "123")
    assert event.name == "worship concert"
    assert event.created_at < datetime.now(timezone.utc)

def test_that_event_name_is_empty_raise_exception(event_service):

    with pytest.raises(ValueError):
        event_service.create_event(CreateEvent(name="", description="worship in spirit and truth", location="Yaba, lagos", organizer_id="123"), "123")

def test_that_event_name_is_blank_raise_exception(event_service):

    with pytest.raises(ValueError):
        event_service.create_event(CreateEvent(name=" ", description="worship in spirit and truth", location="Yaba, lagos", organizer_id="123"), "123")

def test_that_event_location_is_updated_location_changes(event_service):

    created_event = event_service.create_event(
        CreateEvent(name="worship concert", description="worship in spirit and truth", location="Yaba, lagos",
                    organizer_id="123"), "123")

    updated_event = event_service.update_event(created_event.id,
        UpdateEvent(location="Lekki, lagos"))
    assert updated_event.location == "Lekki, lagos"

def test_that_I_find_an_event_with_event_id_returns_event(event_service):

    created_event = event_service.create_event(
        CreateEvent(name="worship concert", description="worship in spirit and truth", location="Yaba, lagos",
                    organizer_id="123"), "123")

    found_event = event_service.find_event(created_event.id)
    assert created_event.id == found_event.id

def test_that_I_find_an_event_with_event_id_that_does_not_exist_raises_exception(event_service):

    with pytest.raises(ValueError):
        event_service.find_event("419")

def test_that_I_create_two_events_repository_has_two_events(event_service):
    created_event_one = event_service.create_event(
        CreateEvent(name="worship concert", description="worship in spirit and truth", location="Yaba, lagos",
                    organizer_id="123"), "123")
    created_event_two = event_service.create_event(
        CreateEvent(name="dance club", description="dance workout", location="Abuja",
                    organizer_id="111"), "111")

    event_list = event_service.get_all_event()
    assert len(event_list) == 2

def test_that_I_an_event_that_exist_it_deletes(event_service):
    created_event = event_service.create_event(
        CreateEvent(name="worship concert", description="worship in spirit and truth", location="Yaba, lagos",
                    organizer_id="123"), "123")

    event_service.delete_event(created_event.id)
    event_list = event_service.get_all_event()
    assert len(event_list) == 0

def test_that_I_an_event_that_does_not_exist_raise_exception(event_service):
    with pytest.raises(ValueError):
        event_service.delete_event(uuid.uuid4())

def test_that_I_create_three_events_I_search_for_tech_keyword_found_two_events(event_service):
    created_event_one = event_service.create_event(
        CreateEvent(name="tech conference", description="worship in spirit and truth", location="Yaba, lagos",
                    organizer_id="123"), "123")
    created_event_two = event_service.create_event(
        CreateEvent(name="women in tech", description="dance workout", location="Abuja",
                    organizer_id="111"), "111")

    created_event_three = event_service.create_event(
        CreateEvent(name="bloom", description="dance workout", location="Surulere",
                    organizer_id="122"), "122")

    event_list = event_service.search_events("tech")
    assert len(event_list) == 2

def test_that_I_create_three_events_I_search_for_tech_keyword_found_three_events(event_service):
    created_event_one = event_service.create_event(
        CreateEvent(name="tech conference", description="worship in spirit and truth", location="Yaba, lagos",
                    organizer_id="123"), "123")
    created_event_two = event_service.create_event(
        CreateEvent(name="women in tech", description="dance workout", location="Abuja",
                    organizer_id="111"), "111")

    created_event_three = event_service.create_event(
        CreateEvent(name="semicolon hangout", description="tech revolution", location="Surulere",
                    organizer_id="122"), "122")

    event_list = event_service.search_events("tech")
    assert len(event_list) == 3

def test_that_I_create_three_events_I_search_for_a_keyword_not_existing_found_zero_events(event_service):
    created_event_one = event_service.create_event(
        CreateEvent(name="tech conference", description="worship in spirit and truth", location="Yaba, lagos",
                    organizer_id="123"), "123")
    created_event_two = event_service.create_event(
        CreateEvent(name="women in tech", description="dance workout", location="Abuja",
                    organizer_id="111"), "111")

    created_event_three = event_service.create_event(
        CreateEvent(name="semicolon hangout", description="tech revolution", location="Surulere",
                    organizer_id="122"), "122")

    event_list = event_service.search_events("grace")
    assert len(event_list) == 0