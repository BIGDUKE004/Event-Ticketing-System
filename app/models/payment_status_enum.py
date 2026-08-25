from enum import Enum

class PaymentStatus(Enum):
    PENDING = "pending"
    SUCCESSFUL = "successful"
    CANCELLED = "cancelled"