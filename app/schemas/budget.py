from pydantic import BaseModel


class BudgetCreate(BaseModel):
    amount: int


class BudgetUpdate(BaseModel):
    amount: int


class BudgetResponse(BaseModel):
    id: int
    amount: int

    model_config = {
        "from_attributes": True
    }