from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from app.db.database import Base
from sqlalchemy.orm import relationship


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    amount = Column(Float, nullable=False)

    type = Column(String, nullable=False)

    category = Column(String, nullable=False)

    date = Column(Date, nullable=False)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )
    owner = relationship(
        "User",
        back_populates="transactions"
    )