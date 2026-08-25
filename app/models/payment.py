from dataclasses import field
from uuid import uuid4, UUID
from xmlrpc.client import DateTime

from pydantic import BaseModel


class Payment(BaseModel):
    id : UUID = field(default_factory=uuid4)
    booking_id : str
    amount : float
    payment_status: payment_status.PaymentStatus
    payment_date: DateTime