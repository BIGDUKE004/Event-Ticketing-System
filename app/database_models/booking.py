import uuid
from datetime import datetime, timezone

from sqlalchemy import Integer, String, ForeignKey, DateTime, Enum, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models import booking_status
from app.database_models.booking_item import BookingItem

class Booking(Base):
    __tablename__ = "booking"

    id: Mapped[uuid.UUID] = mapped_column(
        String(36),
        default=uuid.uuid4,
        primary_key=True,
        nullable=False,
    )

    user_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("user.id"),
        nullable=False,
    )

    event_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("event.id"),
        nullable=False,
    )

    booking_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    bookings: Mapped[list[BookingItem]] = relationship(
        BookingItem,
        backref="booking"
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    total_amount: Mapped[float] = mapped_column(
        Float,
        default=0,
        nullable=False,
    )

    status: Mapped[booking_status.BookingStatus] = mapped_column(
        Enum(booking_status.BookingStatus),
        nullable=False
    )
