from fastapi import APIRouter, status

from app.models.booking import Booking
from app.repositories.in_memory_booking_repository import InMemoryBookingRepository
from app.services.booking_service import BookingService

router = APIRouter(prefix="/booking", tags=["Booking"])

repository = InMemoryBookingRepository()
service = BookingService(repository)

@router.post("/register_booking", response_model=Booking.CreateBookingResponse, status_code=status.HTTP_201_CREATED)
def register(request: Booking.CreateBooking):
    return service.add_booking(request)

@router.post("/update_booking", response_model=Booking.UpdateBookingResponse, status_code=status.HTTP_201_CREATED)
def update(request: Booking.UpdateBooking):
    return service.update_booking(request)

@router.get("/get_booking_information", response_model=Booking.GetBookingInformationResponse, status_code=status.HTTP_201_CREATED)
def get_booking(request: Booking.GetBookingInformation):
    return service.get_booking_information(request)

@router.delete("/delete_booking", response_model=Booking.DeleteBookingResponse, status_code=status.HTTP_201_CREATED)
def delete_booking(request: Booking.DeleteBooking):
    return service.delete_booking(request)