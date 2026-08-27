from typing import List

from app.models.booking import Booking
from app.repositories.booking_repository import BookingRepository


class InMemoryBookingRepository(BookingRepository):
    def __init__(self):
        self.booking_list = []

    def save_booking(self, booking: Booking) -> Booking:
        self.booking_list.append(booking)
        return booking

    def delete_booking(self, user_id: str) -> None:
        for booking in self.booking_list:
            if booking.user_id == user_id:
                self.booking_list.remove(booking)

    def update_booking(self, booking: Booking.UpdateBooking) -> Booking:
        for existing_booking in self.booking_list:
            if str(existing_booking.id) == booking.id:
                existing_booking.user_id = booking.user_id
                existing_booking.event_id = booking.event_id
                existing_booking.ticket_type = booking.ticket_type
                existing_booking.bookings = booking.bookings
                existing_booking.quantity = booking.quantity
                existing_booking.total_amount = booking.total_amount

                return existing_booking

        return None


    def get_all_bookings(self) -> List[Booking]:
        return self.booking_list

    def get_booking_information(self, booking_id: str) -> Booking:
        for bookings in self.booking_list:
            if str(bookings.id) == booking_id:
                return bookings
