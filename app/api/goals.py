from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.goal import Goal
from app.models.user import User
from app.schemas.goal import (
    GoalCreate,
    GoalUpdate,
    GoalResponse
)
from app.core.dependencies import get_current_user

router = APIRouter()


@router.post(
    "/",
    response_model=GoalResponse
)
def create_goal(
    goal: GoalCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    new_goal = Goal(
        title=goal.title,
        target_amount=goal.target_amount,
        user_id=current_user.id
    )

    db.add(new_goal)
    db.commit()
    db.refresh(new_goal)

    return new_goal


@router.get(
    "/",
    response_model=list[GoalResponse]
)
def get_goals(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    goals = (
        db.query(Goal)
        .filter(Goal.user_id == current_user.id)
        .all()
    )

    return goals


@router.put(
    "/{goal_id}",
    response_model=GoalResponse
)
def update_goal(
    goal_id: int,
    goal: GoalUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_goal = (
        db.query(Goal)
        .filter(
            Goal.id == goal_id,
            Goal.user_id == current_user.id
        )
        .first()
    )

    if not db_goal:
        raise HTTPException(
            status_code=404,
            detail="Goal not found"
        )

    db_goal.title = goal.title
    db_goal.target_amount = goal.target_amount
    db_goal.saved_amount = goal.saved_amount

    db.commit()
    db.refresh(db_goal)

    return db_goal


@router.delete("/{goal_id}")
def delete_goal(
    goal_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_goal = (
        db.query(Goal)
        .filter(
            Goal.id == goal_id,
            Goal.user_id == current_user.id
        )
        .first()
    )

    if not db_goal:
        raise HTTPException(
            status_code=404,
            detail="Goal not found"
        )

    db.delete(db_goal)
    db.commit()

    return {
        "message": "Goal deleted successfully"
    }
