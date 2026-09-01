from typing import Optional
from uuid import uuid4, UUID
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models import booking_status
from app.models import booking_item

class Booking:
    class CreateBooking(BaseModel):
        user_id: str
        event_id: str
        bookings : list[booking_item.BookingItem]
        quantity: int
        total_amount: float

    class UpdateBooking(BaseModel):
        id : str
        user_id: Optional[str] = None
        event_id: Optional[str] = None
        bookings : Optional[list[booking_item.BookingItem]] = None
        quantity: Optional[int] = None
        total_amount: Optional[float] = None

    class DeleteBooking(BaseModel):
        id: UUID

    class GetBookingInformation(BaseModel):
        id : UUID

    class CreateBookingResponse(BaseModel):
        model_config = ConfigDict(from_attributes=True)
        id : str
        user_id: str
        booking_date: datetime
        bookings : list[booking_item.BookingItem]
        quantity: int
        total_amount: float
        status: booking_status.BookingStatus

    class UpdateBookingResponse(BaseModel):
        model_config = ConfigDict(from_attributes=True)
        id: str
        user_id: str
        event_id: str
        booking_date: datetime
        bookings: list[booking_item.BookingItem]
        quantity: int
        total_amount: float
        status: booking_status.BookingStatus

    class GetBookingInformationResponse(BaseModel):
        model_config = ConfigDict(from_attributes=True)
        id: str
        user_id: str
        booking_date: datetime
        quantity: int
        bookings: list[booking_item.BookingItem]
        total_amount: float
        status: booking_status.BookingStatus

    class DeleteBookingResponse(BaseModel):
        model_config = ConfigDict(from_attributes=True)
        message : str



