import uuid
from dataclasses import fields

from pydantic import BaseModel


class Ticket(BaseModel):
    id : uuid.UUID = fields(default_factory=uuid.uuid4)
    booking_id : str
    ticket_type_id : str
    ticket_code : str