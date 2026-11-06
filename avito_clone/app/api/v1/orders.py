from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.order import OrderCreate, OrderOut
from app.services import order_service

router = APIRouter()


@router.post("/", response_model=OrderOut, status_code=201)
def create_order(data: OrderCreate, db: Session = Depends(get_db)):
    try:
        return order_service.add_order(
            db,
            data.user_id,
            [item.model_dump() for item in data.items],
        )
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))


@router.get("/", response_model=list[OrderOut])
def get_orders(
    user_id: int | None = None,
    start_date: date | None = None,
    end_date: date | None = None,
    db: Session = Depends(get_db),
):
    try:
        if start_date is not None or end_date is not None:
            if start_date is None or end_date is None:
                raise HTTPException(
                    status_code=422,
                    detail="Укажите обе даты: start_date и end_date.",
                )
            if user_id is not None:
                orders = order_service.get_orders_by_user_id(db, user_id)
                return [
                    order for order in orders
                    if start_date <= order.create_date.date() <= end_date
                ]
            return order_service.get_orders_between_dates(db, start_date, end_date)
        if user_id is not None:
            return order_service.get_orders_by_user_id(db, user_id)
        return order_service.get_orders(db)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.get("/{order_id}", response_model=OrderOut)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = order_service.get_order(db, order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    return order
