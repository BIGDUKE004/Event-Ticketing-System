from enum import Enum
from datetime import datetime
from uuid import uuid4, UUID

from pydantic import BaseModel, Field, ConfigDict


class CreatePayment(BaseModel):
    booking_id : UUID
    amount : float

class PaymentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    booking_id: UUID
    amount: float
    payment_status: Enum
    payment_date: datetime
