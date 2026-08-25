from uuid import uuid4, UUID
from datetime import datetime

from pydantic import BaseModel, Field

from app.models import booking_status


class Booking(BaseModel):
    id : UUID = Field(default_factory=uuid4)
    user_id: str
    event_id: str
    ticket_type: str
    booking_date: datetime
    quantity: int
    total_amount: float
    status: booking_status.BookingStatus