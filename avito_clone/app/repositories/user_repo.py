from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


def create(db: Session, name: str, email: str) -> User:
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_by_id(db: Session, user_id: int):
    return db.get(User, user_id)


def get_by_name(db: Session, name: str):
    statement = select(User).where(User.name.ilike(name))
    return db.scalars(statement).first()


def get_by_email(db: Session, email: str):
    statement = select(User).where(User.email == email)
    return db.scalars(statement).first()


def get_all(db: Session):
    return db.scalars(select(User).order_by(User.id)).all()
