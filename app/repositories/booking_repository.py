from abc import ABC, abstractmethod
from typing import List

from app.models.booking import Booking

class BookingRepository(ABC):
    @abstractmethod
    def save_booking(self, booking: Booking) -> Booking:
        pass

    @abstractmethod
    def update_booking(self, booking : Booking) -> Booking:
        pass

    @abstractmethod
    def delete_booking(self, booking_id : str) -> None:
        pass

    @abstractmethod
    def get_all_bookings(self) -> List[Booking]:
        pass

    @abstractmethod
    def get_booking_information(self, booking_id: str) -> Booking:
        pass

    @abstractmethod
    def find_booking_by_id(self, booking_id : str) -> Booking:
        pass