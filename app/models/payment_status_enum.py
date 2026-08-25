from enum import Enum

class PaymentStaus(Enum):
    PENDING = "pending"
    SUCCESSFUL = "successful"
    CANCELLED = "cancelled"