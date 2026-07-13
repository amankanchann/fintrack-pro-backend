from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    transactions = relationship(
        "Transaction",
        back_populates="owner"

    )
    budget = relationship(
        "Budget",
        back_populates="owner",
        uselist=False
    )
    goals = relationship(
        "Goal",
        back_populates="owner"
    )
