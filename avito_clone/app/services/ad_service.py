from sqlalchemy.orm import Session

from app.repositories import ad_repo, category_repo, user_repo


def create_ad(db: Session, values: dict):
    if user_repo.get_by_id(db, values["owner_id"]) is None:
        raise ValueError("Владелец не найден.")
    if category_repo.get_by_id(db, values["category_id"]) is None:
        raise ValueError("Категория не найдена.")
    return ad_repo.create(db, **values)


def get_ad(db: Session, ad_id: int):
    return ad_repo.get_by_id(db, ad_id)


def get_ads(db: Session, category_id=None):
    return ad_repo.get_all(db, category_id)


def get_ads_by_category(db: Session, category_id: int):
    return ad_repo.get_all(db, category_id)


def delete_ad(db: Session, ad_id: int):
    ad = ad_repo.get_by_id(db, ad_id)
    if ad is None:
        return False
    ad_repo.delete(db, ad)
    return True
