from dataclasses import field
from uuid import UUID, uuid4
from xmlrpc.client import DateTime

from pydantic import BaseModel


class Event(BaseModel):
    id: UUID = field(default_factory=uuid4)
    name: str
    description: str
    location: str
    date: DateTime
    organizer_id : str
    time : DateTime
    sold_out: bool

