from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.payment import Payment


def create(db: Session, order_id: int, amount: int, method: str) -> Payment:
    payment = Payment(order_id=order_id, amount=amount, method=method)
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment


def get_by_id(db: Session, payment_id: int):
    return db.get(Payment, payment_id)


def get_by_order_id(db: Session, order_id: int):
    statement = select(Payment).where(Payment.order_id == order_id)
    return db.scalars(statement).first()


def save(db: Session, payment: Payment):
    db.commit()
    db.refresh(payment)
    return payment
