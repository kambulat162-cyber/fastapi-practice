from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.models.message import Message


def create(db: Session, **values) -> Message:
    message = Message(**values)
    db.add(message)
    db.commit()
    db.refresh(message)
    return message


def get_for_user(db: Session, user_id: int):
    statement = (
        select(Message)
        .where(or_(Message.sender_id == user_id, Message.recipient_id == user_id))
        .order_by(Message.created_at)
    )
    return db.scalars(statement).all()
