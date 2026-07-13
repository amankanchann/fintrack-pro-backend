from fastapi import FastAPI

from app.core.config import settings
from app.api.auth import router as auth_router
from app.api.transactions import router as transaction_router
from app.api.budgets import router as budget_router
from app.api.goals import router as goal_router
from app.api.analytics import router as analytics_router

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

app.include_router(
    budget_router,
    prefix="/budgets",
    tags=["Budgets"]
)

app.include_router(
    transaction_router,
    prefix="/transactions",
    tags=["Transactions"]
)

app.include_router(
    goal_router,
    prefix="/goals",
    tags=["Goals"]
)

app.include_router(
    analytics_router,
    prefix="/analytics",
    tags=["Analytics"]
)


@app.get("/")
def root():
    return {"message": f"Welcome to {settings.app_name} 🚀"}
