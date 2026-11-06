from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.order import Order, OrderItem


def create(db: Session, user_id: int, items: list[OrderItem]) -> Order:
    order = Order(user_id=user_id, sum=sum(item.unit_price * item.quantity for item in items))
    order.order_items = items
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


def get_by_id(db: Session, order_id: int):
    return db.get(Order, order_id)


def get_orders(db: Session, user_id=None, start_date=None, end_date=None):
    statement = select(Order).order_by(Order.create_date)
    if user_id is not None:
        statement = statement.where(Order.user_id == user_id)
    if start_date is not None:
        statement = statement.where(Order.create_date >= start_date)
    if end_date is not None:
        statement = statement.where(Order.create_date < end_date)
    return db.scalars(statement).all()
