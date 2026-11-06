from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class AdCreate(BaseModel):
    title: str = Field(min_length=2, max_length=160)
    description: str = ""
    price: int = Field(ge=0)
    owner_id: int
    category_id: int


class AdOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str
    price: int
    owner_id: int
    category_id: int
    created_at: datetime
