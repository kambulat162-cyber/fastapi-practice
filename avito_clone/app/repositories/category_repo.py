from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.category import Category


def get_all(db: Session):
    return db.scalars(select(Category).order_by(Category.name)).all()


def get_by_id(db: Session, category_id: int):
    return db.get(Category, category_id)


def create_if_missing(db: Session, name: str):
    statement = select(Category).where(Category.name == name)
    category = db.scalars(statement).first()
    if category is None:
        category = Category(name=name)
        db.add(category)
    return category
