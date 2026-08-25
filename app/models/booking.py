from dataclasses import field
from uuid import uuid4, UUID
from xmlrpc.client import DateTime

from pydantic import BaseModel

from app.models import booking_status


class Booking(BaseModel):
    id : UUID = field(default_factory=uuid4)
    user_id: str
    event_id: str
    ticket_type: str
    booking_date: DateTime
    quantity: int
    total_amount: float
    status: booking_status.BookingStatus