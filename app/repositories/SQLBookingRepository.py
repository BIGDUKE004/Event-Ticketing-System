from http.client import HTTPException
from typing import List
from uuid import UUID

from sqlalchemy.orm import Session

from app.repositories.booking_repository import BookingRepository
from app.database_models.booking import Booking


class SQLBookingRepository(BookingRepository):
    def __init__(self, db : Session):
        self.db = db

    def save_booking(self, booking: Booking) -> Booking:
        self.db.add(booking)
        self.db.commit()
        self.db.refresh(booking)
        return booking

    def delete_booking(self, booking_id: str) -> None:
        booking = self.get(booking_id)
        if booking is None:
            raise HTTPException(status_code=404, detail="Booking not found")
        self.db.delete(booking)
        self.db.commit()
        return None

    def update_booking(self, booking: Booking) -> Booking:
        user_booking = self.get(booking.id)
        if user_booking is None:
            raise HTTPException(status_code=404, detail="Booking not found, Register booking")

        for key, value in user_booking.items():
            setattr(user_booking, key, value)

        self.db.commit()
        self.db.refresh(user_booking)
        return user_booking

    def get_all_bookings(self) -> List[Booking]:
        return self.db.query(Booking).all()

    def find_booking_by_id(self, booking_id: UUID) -> Booking:
        booking = self.db.query(Booking).filter(Booking.id == booking_id).first()
        if booking is None:
            raise HTTPException(status_code=404, detail="Booking not found")
        return booking

    def get_booking_information(self, booking_id: UUID) -> Booking:
        booking = self.db.query(Booking).filter(Booking.id == booking_id).first()
        if booking is None:
            raise HTTPException(status_code=404, detail="Booking not found")
        return booking
