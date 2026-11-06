from sqlalchemy.orm import Session

from app.repositories import user_repo


def create_user(db: Session, name: str, email: str):
    if user_repo.get_by_email(db, email):
        raise ValueError("Пользователь с таким email уже существует.")
    return user_repo.create(db, name=name, email=email)


def get_user(db: Session, user_id: int):
    return user_repo.get_by_id(db, user_id)


def get_user_by_name(db: Session, name: str):
    return user_repo.get_by_name(db, name)


def get_users(db: Session):
    return user_repo.get_all(db)
