from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.message import MessageCreate, MessageOut
from app.services import message_service

router = APIRouter()


@router.post("/", response_model=MessageOut, status_code=201)
def send_message(data: MessageCreate, db: Session = Depends(get_db)):
    try:
        return message_service.send_message(db, data.model_dump())
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))


@router.get("/user/{user_id}", response_model=list[MessageOut])
def get_messages(user_id: int, db: Session = Depends(get_db)):
    try:
        return message_service.get_messages_for_user(db, user_id)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
