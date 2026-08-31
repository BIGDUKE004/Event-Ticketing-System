import uuid
from datetime import datetime, timezone

from sqlalchemy import String, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from app.models.payment_status_enum import PaymentStatus


class Payment(Base):
    __tablename__ = 'payment'
    id: Mapped[uuid.UUID] = mapped_column(
        String(36),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False
    )

    booking_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False
    )

    amount: Mapped[float] = mapped_column(
        nullable=False
    )

    payment_status: Mapped[PaymentStatus] = mapped_column(
        Enum(PaymentStatus),
        nullable=False
    )

    payment_date:  Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )