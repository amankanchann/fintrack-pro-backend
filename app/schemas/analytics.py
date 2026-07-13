from pydantic import BaseModel


class SummaryResponse(BaseModel):
    total_income: float
    total_expense: float
    current_balance: float
    monthly_budget: float
    budget_used: float


class CategorySpendingResponse(BaseModel):
    category: str
    amount: float


class GoalProgressResponse(BaseModel):
    title: str
    target_amount: float
    saved_amount: float
    progress: float