from datetime import date

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.ad import AdOut
from app.services import search_service

router = APIRouter()


@router.get("/ads", response_model=list[AdOut])
def search_ads(
    q: str | None = None,
    category_id: int | None = None,
    min_price: int | None = Query(default=None, ge=0),
    max_price: int | None = Query(default=None, ge=0),
    db: Session = Depends(get_db),
):
    try:
        return search_service.search_ads(db, q, category_id, min_price, max_price)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.get("/best-products")
def best_products(
    start_date: date,
    end_date: date,
    db: Session = Depends(get_db),
):
    try:
        rows = search_service.get_best_products_range(db, start_date, end_date)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    return [
        {"ad": AdOut.model_validate(ad), "buy_count": count}
        for ad, count in rows
    ]
