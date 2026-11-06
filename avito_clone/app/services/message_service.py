from sqlalchemy.orm import Session

from app.repositories import ad_repo, message_repo, user_repo


def send_message(db: Session, values: dict):
    if user_repo.get_by_id(db, values["sender_id"]) is None:
        raise ValueError("Отправитель не найден.")
    if user_repo.get_by_id(db, values["recipient_id"]) is None:
        raise ValueError("Получатель не найден.")
    if ad_repo.get_by_id(db, values["ad_id"]) is None:
        raise ValueError("Объявление не найдено.")
    return message_repo.create(db, **values)


def get_messages_for_user(db: Session, user_id: int):
    if user_repo.get_by_id(db, user_id) is None:
        raise ValueError("Пользователь не найден.")
    return message_repo.get_for_user(db, user_id)
