from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.transaction import Transaction
from app.models.budget import Budget
from app.models.user import User
from app.core.dependencies import get_current_user
from sqlalchemy import func
from app.models.goal import Goal
from app.schemas.analytics import (
    SummaryResponse,
    CategorySpendingResponse,
    GoalProgressResponse,
)

router = APIRouter()

@router.get(
    "/summary",
    response_model=SummaryResponse
)

def get_summary(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    transactions = (
        db.query(Transaction)
        .filter(Transaction.user_id == current_user.id)
        .all()
    )

    total_income = sum(
        t.amount
        for t in transactions
        if t.type == "income"
    )

    total_expense = sum(
        t.amount
        for t in transactions
        if t.type == "expense"
    )

    current_balance = total_income - total_expense

    budget = (
        db.query(Budget)
        .filter(Budget.user_id == current_user.id)
        .first()
    )

    monthly_budget = (
        budget.monthly_limit
        if budget
        else 0
    )

    budget_used = (
        (total_expense / monthly_budget) * 100
        if monthly_budget > 0
        else 0
    )

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "current_balance": current_balance,
        "monthly_budget": monthly_budget,
        "budget_used": round(budget_used, 2)
    }

@router.get(
    "/category-spending",
    response_model=list[CategorySpendingResponse]
)

def category_spending(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    results = (
        db.query(
            Transaction.category,
            func.sum(Transaction.amount).label("amount")
        )
        .filter(
            Transaction.user_id == current_user.id,
            Transaction.type == "expense"
        )
        .group_by(Transaction.category)
        .all()
    )

    return [
        {
            "category": category,
            "amount": amount
        }
        for category, amount in results
    ]

@router.get(
    "/goal-progress",
    response_model=list[GoalProgressResponse]
)

def goal_progress(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    goals = (
        db.query(Goal)
        .filter(Goal.user_id == current_user.id)
        .all()
    )

    return [
        {
            "title": goal.title,
            "target_amount": goal.target_amount,
            "saved_amount": goal.saved_amount,
            "progress": round(
                (goal.saved_amount / goal.target_amount) * 100,
                2
            ) if goal.target_amount > 0 else 0
        }
        for goal in goals
    ]