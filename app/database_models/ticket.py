import uuid
from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base



class TicketDB(Base):
    __tablename__ = "ticket"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        nullable=False
    )

    booking_id: Mapped[str] = mapped_column(
        String(36),

        nullable=False
    )

    ticket_type_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("ticket_types.id"),
        nullable=False
    )

    ticket_code: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )