from typing import List

from models.booking import Booking
from repositories.booking_repository import BookingRepository


class InMemoryBookingRepository(BookingRepository):
    def __init__(self):
        self.booking_list = []

    def save_booking(self, booking: Booking) -> Booking:
        self.booking_list.append(booking)

    def delete_booking(self, user_id: id) -> Booking:
        for booking in self.booking_list:
            if booking.user_id == user_id:
                self.booking_list.remove(booking)

    def update_booking(self, booking: Booking) -> Booking:
        for bookings in self.booking_list:
            if bookings.user_id == booking.user_id:
                self.booking_list.append(booking)


    def get_all_bookings(self) -> List[Booking]:
        return self.booking_list

    def get_booking_information(self, booking_id: int) -> Booking:
        for bookings in self.booking_list:
            if bookings.id == booking_id:
                return bookings
