from typing import Optional
from uuid import uuid4, UUID
from datetime import datetime

from pydantic import BaseModel, Field

from app.models import booking_status
from app.models import booking_item
from app.models.booking_status import BookingStatus

class Booking(BaseModel):
    id : UUID = Field(default_factory=uuid4)
    user_id: str
    event_id: str
    ticket_type: str
    booking_date: datetime = Field(default_factory=datetime.now)
    bookings : list[booking_item.BookingItem]
    quantity: int
    total_amount: float
    status: booking_status.BookingStatus = Field(default=booking_status.BookingStatus.PENDING)


    class CreateBooking(BaseModel):
        user_id: str
        event_id: str
        ticket_type: str
        bookings : list[booking_item.BookingItem]
        quantity: int
        total_amount: float

    class UpdateBooking(BaseModel):
        id : str
        user_id: Optional[str] = None
        event_id: Optional[str] = None
        ticket_type: Optional[str] = None
        bookings : Optional[list[booking_item.BookingItem]] = None
        quantity: Optional[int] = None
        total_amount: Optional[float] = None

    class DeleteBooking(BaseModel):
        id: UUID

    class GetBookingInformation(BaseModel):
        id : UUID

    class CreateBookingResponse(BaseModel):
        id : str
        ticket_type : str
        user_id: str
        booking_date: datetime
        bookings : list[booking_item.BookingItem]
        quantity: int
        total_amount: float
        status: booking_status.BookingStatus

    class UpdateBookingResponse(BaseModel):
        id: str
        user_id: str
        event_id: str
        ticket_type: str
        booking_date: datetime
        bookings: list[booking_item.BookingItem]
        quantity: int
        total_amount: float
        status: booking_status.BookingStatus

    class GetBookingInformationResponse(BaseModel):
        id: str
        user_id: str
        ticket_type: str
        booking_date: datetime
        quantity: int
        bookings: list[booking_item.BookingItem]
        total_amount: float
        status: booking_status.BookingStatus

    class DeleteBookingResponse(BaseModel):
        message : str



