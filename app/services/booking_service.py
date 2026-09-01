
from fastapi import HTTPException

from app.database_models.booking import Booking
from app.database_models.booking_item import BookingItem
from app.repositories.booking_repository import BookingRepository
from app.models import booking_status


class BookingService:
    def __init__(self, repository : BookingRepository):
        self.__repository = repository

    def add_booking(self, request: Booking) -> Booking:
        total = 0
        for amount in request.bookings:
            if amount.total_amount == 0:
                raise HTTPException("Invalid amount", 400)
            else:
                total = total + amount.total_amount * amount.quantity

        booking_items = []
        for item in request.bookings:
            booking_items.append(BookingItem(
                ticket_type_id=item.ticket_type_id,
                quantity=item.quantity,
                total_amount=item.total_amount
            )
            )
        user_booking = Booking(
            user_id= request.user_id,
            event_id= request.event_id,
            ticket_type= request.ticket_type,
            bookings= booking_items,
            quantity= request.quantity,
            total_amount= total,
            status= booking_status.BookingStatus.PENDING
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

    def update_booking(self, request: Booking) -> Booking:

        total = 0
        for amount in request.bookings:
            if amount.total_amount == 0:
                raise HTTPException("Invalid amount", 400)
            else:
                total = total + amount.total_amount * amount.quantity

        total_quantity = 0
        for quantity in request.bookings:
            total_quantity += quantity.quantity

        user_booking = Booking.UpdateBooking(
            id=request.id,
            user_id=request.user_id,
            event_id=request.event_id,
            ticket_type=request.ticket_type,
            bookings=request.bookings,
            quantity=total_quantity,
            total_amount=total
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

    def delete_booking(self, request: Booking) -> str:
        if self.__repository.find_booking_by_id(request.id) == None:
            raise HTTPException(status_code=404, detail="Booking not found")
        else:
            self.__repository.delete_booking(request.id)

        response : Booking.DeleteBookingResponse = Booking.DeleteBookingResponse(
            message= "Booking deleted",
        )
        return response

    def get_booking_information(self, request: Booking ) -> Booking:

        booking = self.__repository.get_booking_information(request.id)

        if booking is None:
            raise HTTPException(status_code=404, detail="Booking not found")

        response = Booking.GetBookingInformationResponse(
            id=str(booking.id),
            ticket_type=booking.ticket_type,
            total_amount=booking.total_amount,
            user_id=booking.user_id,
            booking_date=booking.booking_date,
            bookings=booking.bookings,
            quantity=booking.quantity,
            status=booking.status,
        )

        return response