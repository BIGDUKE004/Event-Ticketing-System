from typing import Optional

from fastapi import HTTPException

from app.database_models.booking import Booking
from app.models.booking import Booking as model_booking
from app.database_models.booking_item import BookingItem
from app.repositories.booking_repository import BookingRepository
from app.models import booking_status
from app.models import booking_item as model_booking_item
from app.models.ticket_type import TicketType
from app.repositories.ticket_type_repository import TicketTypeRepository


class BookingService:
    def __init__(self, repository : BookingRepository, ticket_type_repo : TicketTypeRepository):
        self.__repository = repository
        self.__ticketTypeRepository = ticket_type_repo

    def reduce_ticket_quantity(self, booking : Booking):
        for booked_item in booking.bookings:
            ticket_type : Optional[TicketType]= self.__ticketTypeRepository.get_by_id(booked_item.ticket_type_id)

            if ticket_type is None:
                raise HTTPException(
                    status_code=404,
                    detail="Ticket type not found"
                )

            if ticket_type.available_quantity < booked_item.quantity:
                raise HTTPException(
                    status_code=400,
                    detail="Not enough tickets available"
                )

            ticket_type.available_quantity -= booked_item.quantity

    def add_booking(self, request: Booking) -> model_booking.CreateBookingResponse:
        total = 0
        for amount in request.bookings:
            if amount.total_amount == 0:
                raise HTTPException("Invalid amount", 400)
            else:
                total = total + amount.total_amount * amount.quantity

        total_quantity = 0
        for quantity in request.bookings:
            if quantity.quantity == 0:
                raise HTTPException("Invalid amount", 400)
            else:
                total_quantity = total_quantity + quantity.quantity

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
            bookings= booking_items,
            quantity= total_quantity,
            total_amount= total,
            status= booking_status.BookingStatus.PENDING
        )
        self.reduce_ticket_quantity(user_booking)
        booking : Booking = self.__repository.save_booking(user_booking)

        converted_bookings = []
        for item in booking.bookings:
            converted_item = model_booking_item.BookingItem.model_validate(item)
            converted_bookings.append(converted_item)

        response : model_booking.CreateBookingResponse = model_booking.CreateBookingResponse(
            id= str(booking.id),
            user_id= booking.user_id,
            booking_date= booking.booking_date,
            bookings= converted_bookings,
            quantity= booking.quantity,
            status= booking.status,
            total_amount=booking.total_amount,
        )
        return response

    def update_booking(self, request: Booking) -> model_booking.UpdateBookingResponse:
        total = 0
        for amount in request.bookings:
            if amount.total_amount == 0:
                raise HTTPException("Invalid amount", 400)
            else:
                total = total + amount.total_amount * amount.quantity

        total_quantity = 0
        for quantity in request.bookings:
            total_quantity += quantity.quantity

        user_booking  = Booking(
            id=request.id,
            user_id=request.user_id,
            event_id=request.event_id,
            bookings=request.bookings,
            quantity=total_quantity,
            total_amount=total
        )

        booking : model_booking.UpdateBookingResponse = self.__repository.update_booking(user_booking)
        converted_bookings = []
        for item in booking.bookings:
            converted_item = model_booking_item.BookingItem.model_validate(item)
            converted_bookings.append(converted_item)
        response = model_booking.UpdateBookingResponse = model_booking.UpdateBookingResponse(
            id=str(booking.id),
            user_id=booking.user_id,
            event_id=booking.event_id,
            booking_date=booking.booking_date,
            bookings=converted_bookings,
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

        response : model_booking.DeleteBookingResponse = model_booking.DeleteBookingResponse(
            message= "Booking deleted",
        )
        return response.message

    def get_booking_information(self, request: Booking ) -> Booking:

        booking = self.__repository.get_booking_information(request.id)

        if booking is None:
            raise HTTPException(status_code=404, detail="Booking not found")

        converted_bookings = []
        for item in booking.bookings:
            converted_item = model_booking_item.BookingItem.model_validate(item)
            converted_bookings.append(converted_item)
        response = Booking.GetBookingInformationResponse(
            id=str(booking.id),
            total_amount=booking.total_amount,
            user_id=booking.user_id,
            booking_date=booking.booking_date,
            bookings=converted_bookings,
            quantity=booking.quantity,
            status=booking.status,
        )

        return response