import uuid
from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, String, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class Event(Base):
    __tablename__ = 'event'
    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    location: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    organizer_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False
    )

    sold_out: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )