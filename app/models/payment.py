from uuid import uuid4, UUID
from datetime import datetime, timezone

from pydantic import BaseModel, Field

from app.models import payment_status_enum


class Payment(BaseModel):
    id : UUID = Field(default_factory=uuid4)
    booking_id : str
    amount : float
    payment_status: payment_status_enum.PaymentStatus
    payment_date: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )