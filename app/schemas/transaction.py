from datetime import date
from pydantic import BaseModel



class TransactionCreate(BaseModel):
    title: str
    amount: float
    type: str
    category: str
    date: date

class TransactionUpdate(BaseModel):
    title: str
    amount: float
    type: str
    category: str
    date: date


class TransactionResponse(BaseModel):
    id: int
    title: str
    amount: float
    type: str
    category: str
    date: date

    model_config = {
        "from_attributes": True
    }