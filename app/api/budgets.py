from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.budget import Budget
from app.models.user import User
from app.schemas.budget import (
    BudgetCreate,
    BudgetUpdate,
    BudgetResponse,
)
from app.core.dependencies import get_current_user

router = APIRouter()


@router.post(
    "/",
    response_model=BudgetResponse
)
def create_budget(
    budget: BudgetCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    existing_budget = (
        db.query(Budget)
        .filter(Budget.user_id == current_user.id)
        .first()
    )

    if existing_budget:
        raise HTTPException(
            status_code=400,
            detail="Budget already exists",
        )

    new_budget = Budget(
        amount=budget.amount,
        user_id=current_user.id,
    )

    db.add(new_budget)
    db.commit()
    db.refresh(new_budget)

    return new_budget


@router.get(
    "/",
    response_model=BudgetResponse
)
def get_budget(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    budget = (
        db.query(Budget)
        .filter(Budget.user_id == current_user.id)
        .first()
    )

    if not budget:
        raise HTTPException(
            status_code=404,
            detail="Budget not found",
        )

    return budget


@router.put(
    "/",
    response_model=BudgetResponse
)
def update_budget(
    budget: BudgetUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    db_budget = (
        db.query(Budget)
        .filter(Budget.user_id == current_user.id)
        .first()
    )

    if not db_budget:
        raise HTTPException(
            status_code=404,
            detail="Budget not found",
        )

    db_budget.amount = budget.amount

    db.commit()
    db.refresh(db_budget)

    return db_budget