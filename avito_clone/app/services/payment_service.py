from sqlalchemy.orm import Session

from app.repositories import order_repo, payment_repo


def create_payment(db: Session, order_id: int, method: str):
    order = order_repo.get_by_id(db, order_id)
    if order is None:
        raise ValueError("Заказ не найден.")
    if payment_repo.get_by_order_id(db, order_id) is not None:
        raise ValueError("Для этого заказа платеж уже создан.")
    return payment_repo.create(db, order_id, order.sum, method)


def complete_payment(db: Session, payment_id: int):
    payment = payment_repo.get_by_id(db, payment_id)
    if payment is None:
        raise ValueError("Платеж не найден.")
    if payment.status == "pending":
        payment.status = "paid"
        payment_repo.save(db, payment)
    return payment
