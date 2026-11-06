from datetime import date

from sqlalchemy.orm import Session

from app.repositories import ad_repo


def search_ads(db: Session, query=None, category_id=None, min_price=None, max_price=None):
    if min_price is not None and max_price is not None and min_price > max_price:
        raise ValueError("Минимальная цена не может быть выше максимальной.")
    return ad_repo.search(db, query, category_id, min_price, max_price)


def get_best_products_range(db: Session, start_date: date, end_date: date):
    if start_date > end_date:
        raise ValueError("Начальная дата не должна быть позже конечной.")
    return ad_repo.best_products_range(db, start_date, end_date)
