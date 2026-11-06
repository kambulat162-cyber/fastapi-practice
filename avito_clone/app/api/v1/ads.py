from fastapi import APIRouter, Depends, HTTPException, Query, Response
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.ad import AdCreate, AdOut
from app.services import ad_service

router = APIRouter()


@router.post("/", response_model=AdOut, status_code=201)
def create_ad(data: AdCreate, db: Session = Depends(get_db)):
    try:
        return ad_service.create_ad(db, data.model_dump())
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))


@router.get("/", response_model=list[AdOut])
def get_ads(
    category_id: int | None = Query(default=None),
    db: Session = Depends(get_db),
):
    return ad_service.get_ads(db, category_id)


@router.get("/{ad_id}", response_model=AdOut)
def get_ad(ad_id: int, db: Session = Depends(get_db)):
    ad = ad_service.get_ad(db, ad_id)
    if ad is None:
        raise HTTPException(status_code=404, detail="Объявление не найдено")
    return ad


@router.delete("/{ad_id}", status_code=204)
def delete_ad(ad_id: int, db: Session = Depends(get_db)):
    if not ad_service.delete_ad(db, ad_id):
        raise HTTPException(status_code=404, detail="Объявление не найдено")
    return Response(status_code=204)
