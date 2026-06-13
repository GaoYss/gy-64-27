from datetime import date
from typing import Literal

from pydantic import BaseModel, Field


PaymentStatus = Literal["pending", "received", "partial", "overdue"]


class PaymentBase(BaseModel):
    project_id: int
    project_name: str
    amount: float = Field(gt=0)
    payment_date: date
    status: PaymentStatus = "pending"
    notes: str = ""


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    project_id: int | None = None
    project_name: str | None = None
    amount: float | None = Field(default=None, gt=0)
    payment_date: date | None = None
    status: PaymentStatus | None = None
    notes: str | None = None


class Payment(PaymentBase):
    id: int
