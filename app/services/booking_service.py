from models.booking import Booking
from repositories.booking_repository import BookingRepository
from routers.auth_router import repository


class BookingService:
    def __init__(self, repository : BookingRepository):
        self.__repository = repository

    def add_booking(self, request: Booking):