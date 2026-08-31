import uuid

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from database import Base
from database_models.booking import Booking


class BookingItem(Base):
    __tablename__ = 'booking_item'
    ticket_type_id = Column(
        Integer,
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False
    )

    quantity : Mapped[str] = mapped_column(
        String(36),
        default=0,
        nullable=False
    )

    total_amount : Mapped[float] = mapped_column(
        Float,
        default=0,
        nullable=False
    )

    booking: Mapped["Booking"] = relationship(
        "Booking",
        back_populates="bookings"
    )

