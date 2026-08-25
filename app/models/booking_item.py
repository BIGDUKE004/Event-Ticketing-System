from pydantic import BaseModel


class BookingItem(BaseModel):
    ticket_type_id: str
    quantity: int
    total_amount: int