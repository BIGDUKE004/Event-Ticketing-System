import uuid

from pydantic import BaseModel, Field


class Ticket(BaseModel):
    id : uuid.UUID = Field(default_factory=uuid.uuid4)
    booking_id : str
    ticket_type_id : str
    ticket_code : str