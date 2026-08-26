from typing import Optional
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

    class CreateBooking(BaseModel):
        user_id: str
        event_id: str
        ticket_type: str
        quantity: int
        total_amount: float

    class UpdateBooking(BaseModel):
        user_id: Optional[str] = None
        event_id: Optional[str] = None
        ticket_type: Optional[str] = None
        quantity: Optional[int] = None
        total_amount: Optional[float] = None

    class DeleteBooking(BaseModel):
        id: UUID    

