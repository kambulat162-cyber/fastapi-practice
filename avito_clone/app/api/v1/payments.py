from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.payment import PaymentCreate, PaymentOut
from app.services import payment_service

router = APIRouter()


@router.post("/", response_model=PaymentOut, status_code=201)
def create_payment(data: PaymentCreate, db: Session = Depends(get_db)):
    try:
        return payment_service.create_payment(db, data.order_id, data.method)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.post("/{payment_id}/complete", response_model=PaymentOut)
def complete_payment(payment_id: int, db: Session = Depends(get_db)):
    try:
        return payment_service.complete_payment(db, payment_id)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
