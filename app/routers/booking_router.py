from fastapi import APIRouter, status, Depends

from app.models.booking import Booking
from app.services.booking_service import BookingService
from app.dependencies import get_booking_service

router = APIRouter(prefix="/booking", tags=["Booking"])


@router.post("/register_booking", response_model=Booking.CreateBookingResponse, status_code=status.HTTP_201_CREATED)
def register(request: Booking.CreateBooking, service : BookingService = Depends(get_booking_service)):
    return service.add_booking(request)

@router.post("/update_booking", response_model=Booking.UpdateBookingResponse, status_code=status.HTTP_201_CREATED)
def update(request: Booking.UpdateBooking,  service : BookingService = Depends(get_booking_service)):
    return service.update_booking(request)

@router.get("/get_booking_information", response_model=Booking.GetBookingInformationResponse, status_code=status.HTTP_201_CREATED)
def get_booking(request: Booking.GetBookingInformation,  service : BookingService = Depends(get_booking_service)):
    return service.get_booking_information(request)

@router.delete("/delete_booking", response_model=Booking.DeleteBookingResponse, status_code=status.HTTP_201_CREATED)
def delete_booking(request: Booking.DeleteBooking,  service : BookingService = Depends(get_booking_service)):
    return service.delete_booking(request)