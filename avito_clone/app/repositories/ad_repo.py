from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.ad import Ad
from app.models.order import Order, OrderItem


def create(db: Session, **values) -> Ad:
    ad = Ad(**values)
    db.add(ad)
    db.commit()
    db.refresh(ad)
    return ad


def get_by_id(db: Session, ad_id: int):
    return db.get(Ad, ad_id)


def get_all(db: Session, category_id=None):
    statement = select(Ad).order_by(Ad.id)
    if category_id is not None:
        statement = statement.where(Ad.category_id == category_id)
    return db.scalars(statement).all()


def search(db: Session, query=None, category_id=None, min_price=None, max_price=None):
    statement = select(Ad)
    if query:
        statement = statement.where(Ad.title.ilike(f"%{query}%"))
    if category_id is not None:
        statement = statement.where(Ad.category_id == category_id)
    if min_price is not None:
        statement = statement.where(Ad.price >= min_price)
    if max_price is not None:
        statement = statement.where(Ad.price <= max_price)
    return db.scalars(statement.order_by(Ad.id)).all()


def delete(db: Session, ad: Ad):
    db.delete(ad)
    db.commit()


def best_products_range(db: Session, start_date, end_date):
    statement = (
        select(Ad, func.sum(OrderItem.quantity).label("buy_count"))
        .join(OrderItem, OrderItem.ad_id == Ad.id)
        .join(Order, Order.id == OrderItem.order_id)
        .where(func.date(Order.create_date) >= start_date)
        .where(func.date(Order.create_date) <= end_date)
        .group_by(Ad.id)
        .order_by(func.sum(OrderItem.quantity).desc())
    )
    return db.execute(statement).all()
