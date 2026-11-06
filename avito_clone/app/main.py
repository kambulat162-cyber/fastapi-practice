from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import router as v1_router
from app.config import CORS_ORIGINS
from app.database import Base, SessionLocal, engine
from app.models import Ad, Category, Message, Order, OrderItem, Payment, User
from app.repositories.category_repo import create_if_missing


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    with SessionLocal.begin() as db:
        for name in ("Электроника", "Дом", "Одежда", "Спорт", "Книги", "Другое"):
            create_if_missing(db, name)
    yield


app = FastAPI(title="Avito Clone API", version="1.0.0", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in CORS_ORIGINS if origin.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(v1_router, prefix="/api/v1")


@app.get("/")
def root():
    return {"name": "Avito Clone API", "docs": "/docs"}
