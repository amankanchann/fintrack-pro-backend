from datetime import datetime
from pydantic import BaseModel, Field


class GoalCreate(BaseModel):
    title: str
    target_amount: float = Field(gt=0)


class GoalUpdate(BaseModel):
    title: str
    target_amount: float = Field(gt=0)
    saved_amount: float = Field(ge=0)


class GoalResponse(BaseModel):
    id: int
    title: str
    target_amount: float
    saved_amount: float
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }