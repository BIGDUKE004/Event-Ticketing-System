from typing import Optional, List
from uuid import UUID

from sqlalchemy.orm import Session

from app.database_models.payment import Payment as PaymentModel
from app.repositories.payment_repository import PaymentRepository


class SQLPaymentRepository(PaymentRepository):

    def __init__(self, db: Session):
        self.db = db

    def add(self, payment: PaymentModel):
        self.db.add(payment)
        self.db.commit()
        self.db.refresh(payment)
        return payment

    def get(self, payment_id: UUID) -> Optional[PaymentModel]:
        payment = self.db.query(PaymentModel).filter(PaymentModel.id == str(payment_id)).first()
        if payment is None:
            return None
        return payment

    def get_all(self) :
        return self.db.query(PaymentModel).all()
