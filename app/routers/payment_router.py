from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, status, HTTPException

from app.dependencies import get_payment_service
from app.models.payment import CreatePayment, PaymentResponse
from app.services.payment_service import PaymentService

router = APIRouter(prefix="/payments", tags=["Payments"])

@router.post("/", response_model=PaymentResponse, status_code=status.HTTP_201_CREATED)
def create_payment(
    payload: CreatePayment,
    service: PaymentService = Depends(get_payment_service),
):
    return service.process_payment(payload)

@router.get("/", response_model=List[PaymentResponse])
def get_all_payment(
    service: PaymentService = Depends(get_payment_service)
):
    return service.get_all_payments()

@router.get("/{booking_id}", response_model=PaymentResponse)
def get_booking_payment(
    booking_id: UUID,
    service: PaymentService = Depends(get_payment_service),
):
    try:
        return service.get_booking_payment(booking_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))