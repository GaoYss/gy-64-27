from fastapi import APIRouter

from app.schemas.payments import Payment, PaymentCreate, PaymentUpdate
from app.services.payments import payment_service

router = APIRouter(prefix="/api/payments", tags=["payments"])


@router.get("", response_model=list[Payment])
def list_payments() -> list[dict]:
    return payment_service.list()


@router.post("", response_model=Payment, status_code=201)
def create_payment(payload: PaymentCreate) -> dict:
    return payment_service.create(payload)


@router.patch("/{payment_id}", response_model=Payment)
def update_payment(payment_id: int, payload: PaymentUpdate) -> dict:
    return payment_service.update(payment_id, payload)
