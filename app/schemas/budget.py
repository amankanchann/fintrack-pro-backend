from datetime import datetime
from pydantic import BaseModel, Field


class BudgetCreate(BaseModel):
    monthly_limit: float = Field(gt=0)


class BudgetUpdate(BaseModel):
    monthly_limit: float = Field(gt=0)


class BudgetResponse(BaseModel):
    id: int
    monthly_limit: float
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }