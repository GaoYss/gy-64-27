from typing import Any

from pydantic import BaseModel


class FinancialSummary(BaseModel):
    total_budget: float
    total_procurement: float
    total_payments_received: float
    total_gross_profit: float
    overall_margin: float


class ProjectCostItem(BaseModel):
    project_id: int
    project_name: str
    customer_name: str
    budget: float
    procurement_total: float
    payment_received: float
    gross_profit: float
    gross_margin: float


class DashboardSummary(BaseModel):
    generated_at: str
    metrics: list[dict[str, Any]]
    procurement_budget: float
    financial_summary: FinancialSummary
    project_costs: list[ProjectCostItem]
    phase_distribution: list[dict[str, Any]]
    recent_updates: list[dict[str, Any]]
