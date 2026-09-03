import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class CreateTicket(BaseModel):
    booking_id : str
    ticket_type_id : str
    ticket_code : str

class Ticket(BaseModel):
    id : uuid.UUID = Field(default_factory=uuid.uuid4)
    booking_id : str
    ticket_type_id : str
    ticket_code: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

