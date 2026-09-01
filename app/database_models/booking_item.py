import uuid

from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class BookingItem(Base):
    __tablename__ = "booking_item"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        nullable=False
    )

    booking_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("booking.id"),
        nullable=False
    )

    ticket_type_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("ticket_types.id"),
        nullable=False
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False
    )

    total_amount: Mapped[float] = mapped_column(
        Float,
        default=0,
        nullable=False
    )