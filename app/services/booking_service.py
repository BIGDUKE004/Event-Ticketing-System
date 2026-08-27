from app.models.booking import Booking
from app.repositories.booking_repository import BookingRepository


class BookingService:
    def __init__(self, repository : BookingRepository):
        self.__repository = repository

    def add_booking(self, request: Booking.CreateBooking) -> Booking.CreateBookingResponse:
        user_booking = Booking(
            user_id= request.user_id,
            event_id= request.event_id,
            ticket_type= request.ticket_type,
            bookings= request.bookings,
            quantity= request.quantity,
            total_amount= request.total_amount
        )
        booking : Booking = self.__repository.save_booking(user_booking)
        response : Booking.CreateBookingResponse = Booking.CreateBookingResponse(
            id= str(booking.id),
            ticket_type= booking.ticket_type,
            user_id= booking.user_id,
            booking_date= booking.booking_date,
            bookings= booking.bookings,
            quantity= booking.quantity,
            status= booking.status,
            total_amount=booking.total_amount,
        )
        return response

    def update_booking(self, request: Booking.UpdateBooking) -> Booking.UpdateBookingResponse:
        user_booking = Booking.UpdateBooking(
            id=request.id,
            user_id=request.user_id,
            event_id=request.event_id,
            ticket_type=request.ticket_type,
            bookings=request.bookings,
            quantity=request.quantity,
            total_amount=request.total_amount
        )
        booking : Booking = self.__repository.update_booking(user_booking)
        response = Booking.UpdateBookingResponse = Booking.UpdateBookingResponse(
            id=str(booking.id),
            ticket_type=booking.ticket_type,
            user_id=booking.user_id,
            event_id=booking.event_id,
            booking_date=booking.booking_date,
            bookings=booking.bookings,
            quantity=booking.quantity,
            total_amount=booking.total_amount,
            status=booking.status
        )
        return response

    def delete_booking(self, request: Booking.DeleteBooking) -> Booking.DeleteBookingResponse:
        self.__repository.delete_booking(request.id)
        response : Booking.DeleteBookingResponse = Booking.DeleteBookingResponse(
            message= "Booking deleted",
        )
        return response

    def get_booking_information(self, request : Booking.GetBookingInformation) -> Booking.GetBookingInformationResponse:
        booking : Booking = self.__repository.get_booking_information(request.id)
        response : Booking.GetBookingInformationResponse = Booking.GetBookingInformationResponse(
            id= booking.id,
            ticket_type= booking.ticket_type,
            total_amount= booking.total_amount,
            user_id= booking.user_id,
            booking_date= booking.booking_date,
            bookings= booking.bookings,
            quantity= booking.quantity,
            status= booking.status,
        )
        return response