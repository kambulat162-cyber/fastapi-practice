from sqlalchemy.orm import Session

from app.repositories import category_repo


def get_categories(db: Session):
    return category_repo.get_all(db)
