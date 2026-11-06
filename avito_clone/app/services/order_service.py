from datetime import date, datetime, time, timedelta

from sqlalchemy.orm import Session

from app.models.order import OrderItem
from app.repositories import ad_repo, order_repo, user_repo


def add_order(db: Session, user_id: int, requested_items: list[dict]):
    if user_repo.get_by_id(db, user_id) is None:
        raise ValueError("Пользователь не найден.")

    items = []
    for requested_item in requested_items:
        ad = ad_repo.get_by_id(db, requested_item["ad_id"])
        if ad is None:
            raise ValueError(f"Объявление {requested_item['ad_id']} не найдено.")
        items.append(OrderItem(
            ad_id=ad.id,
            quantity=requested_item["quantity"],
            unit_price=ad.price,
        ))
    return order_repo.create(db, user_id, items)


def get_order(db: Session, order_id: int):
    return order_repo.get_by_id(db, order_id)


def get_orders(db: Session):
    return order_repo.get_orders(db)


def get_orders_by_user_id(db: Session, user_id: int):
    if user_repo.get_by_id(db, user_id) is None:
        raise ValueError("Пользователь не найден.")
    return order_repo.get_orders(db, user_id=user_id)


def get_orders_between_dates(db: Session, start_date: date, end_date: date):
    if start_date > end_date:
        raise ValueError("Начальная дата не должна быть позже конечной.")
    end_exclusive = datetime.combine(end_date + timedelta(days=1), time.min)
    return order_repo.get_orders(
        db,
        start_date=datetime.combine(start_date, time.min),
        end_date=end_exclusive,
    )
