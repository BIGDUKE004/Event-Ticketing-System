from pydantic import BaseModel, ConfigDict


class BookingItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    ticket_type_id: str
    quantity: int
    total_amount: float
