from copy import deepcopy
from datetime import date, datetime, timedelta
from itertools import count
from typing import Any


class InMemoryStore:
    def __init__(self) -> None:
        today = date.today()
        self._counters = {
            "customers": count(4),
            "appointments": count(4),
            "projects": count(4),
            "procurements": count(4),
            "inspections": count(4),
            "payments": count(4),
        }
        self.customers: list[dict[str, Any]] = [
            {
                "id": 1,
                "name": "Chen Wei",
                "phone": "13800010001",
                "community": "Riverside Garden",
                "house_type": "3 bed 2 bath",
                "source": "Referral",
                "budget": 280000,
                "status": "contacted",
                "reported_at": str(today - timedelta(days=16)),
                "owner": "Lina",
                "notes": "Prefers modern minimalist style.",
            },
            {
                "id": 2,
                "name": "Wang Min",
                "phone": "13800010002",
                "community": "Lakeview Mansion",
                "house_type": "Duplex",
                "source": "Online ad",
                "budget": 520000,
                "status": "measured",
                "reported_at": str(today - timedelta(days=9)),
                "owner": "Kai",
                "notes": "Needs full-house smart lighting quote.",
            },
            {
                "id": 3,
                "name": "Liu Fang",
                "phone": "13800010003",
                "community": "North Star Residence",
                "house_type": "2 bed 1 bath",
                "source": "Walk-in",
                "budget": 180000,
                "status": "signed",
                "reported_at": str(today - timedelta(days=4)),
                "owner": "Mia",
                "notes": "Contract signed, construction starts soon.",
            },
        ]
        self.appointments: list[dict[str, Any]] = [
            {
                "id": 1,
                "customer_id": 1,
                "customer_name": "Chen Wei",
                "address": "Riverside Garden B2-1201",
                "scheduled_at": f"{today + timedelta(days=1)}T10:00:00",
                "designer": "Qiao",
                "surveyor": "Hao",
                "status": "scheduled",
                "requirements": "Check load-bearing walls and balcony drainage.",
            },
            {
                "id": 2,
                "customer_id": 2,
                "customer_name": "Wang Min",
                "address": "Lakeview Mansion 8-302",
                "scheduled_at": f"{today + timedelta(days=2)}T14:30:00",
                "designer": "Yun",
                "surveyor": "Hao",
                "status": "scheduled",
                "requirements": "Bring laser measure and smart home checklist.",
            },
            {
                "id": 3,
                "customer_id": 3,
                "customer_name": "Liu Fang",
                "address": "North Star Residence 6-808",
                "scheduled_at": f"{today - timedelta(days=1)}T09:30:00",
                "designer": "Qiao",
                "surveyor": "Jun",
                "status": "completed",
                "requirements": "Dimensions confirmed.",
            },
        ]
        self.projects: list[dict[str, Any]] = [
            {
                "id": 1,
                "customer_name": "Liu Fang",
                "project_name": "North Star Residence Renovation",
                "manager": "Zhou",
                "phase": "demolition",
                "progress": 18,
                "start_date": str(today - timedelta(days=3)),
                "expected_finish": str(today + timedelta(days=57)),
                "risk_level": "low",
                "latest_update": "Demolition area protected, waste removal booked.",
                "budget": 180000,
            },
            {
                "id": 2,
                "customer_name": "Sun Jie",
                "project_name": "Central Park Apartment",
                "manager": "Tang",
                "phase": "waterproofing",
                "progress": 46,
                "start_date": str(today - timedelta(days=24)),
                "expected_finish": str(today + timedelta(days=36)),
                "risk_level": "medium",
                "latest_update": "Bathroom waterproofing needs second inspection.",
                "budget": 350000,
            },
            {
                "id": 3,
                "customer_name": "Zhao Lei",
                "project_name": "Harbor Loft",
                "manager": "Zhou",
                "phase": "finishing",
                "progress": 82,
                "start_date": str(today - timedelta(days=48)),
                "expected_finish": str(today + timedelta(days=12)),
                "risk_level": "low",
                "latest_update": "Cabinet installation completed.",
                "budget": 420000,
            },
        ]
        self.procurements: list[dict[str, Any]] = [
            {
                "id": 1,
                "project_id": 1,
                "project_name": "North Star Residence Renovation",
                "material": "Cement board",
                "supplier": "Jintai Building Materials",
                "quantity": 80,
                "unit": "sheets",
                "budget": 9600,
                "status": "ordered",
                "required_date": str(today + timedelta(days=5)),
            },
            {
                "id": 2,
                "project_id": 2,
                "project_name": "Central Park Apartment",
                "material": "Waterproof coating",
                "supplier": "Green Shield",
                "quantity": 24,
                "unit": "buckets",
                "budget": 7200,
                "status": "delivered",
                "required_date": str(today - timedelta(days=2)),
            },
            {
                "id": 3,
                "project_id": 3,
                "project_name": "Harbor Loft",
                "material": "Oak flooring",
                "supplier": "Nature Wood",
                "quantity": 110,
                "unit": "sqm",
                "budget": 38500,
                "status": "pending",
                "required_date": str(today + timedelta(days=8)),
            },
        ]
        self.inspections: list[dict[str, Any]] = [
            {
                "id": 1,
                "project_id": 1,
                "project_name": "North Star Residence Renovation",
                "inspection_type": "Site protection",
                "scheduled_date": str(today),
                "inspector": "An",
                "result": "passed",
                "issues": "Protection film installed correctly.",
            },
            {
                "id": 2,
                "project_id": 2,
                "project_name": "Central Park Apartment",
                "inspection_type": "Waterproofing",
                "scheduled_date": str(today + timedelta(days=1)),
                "inspector": "An",
                "result": "pending",
                "issues": "Awaiting 48-hour closed-water test.",
            },
            {
                "id": 3,
                "project_id": 3,
                "project_name": "Harbor Loft",
                "inspection_type": "Woodwork",
                "scheduled_date": str(today - timedelta(days=2)),
                "inspector": "Mo",
                "result": "整改",
                "issues": "One cabinet door gap exceeds tolerance.",
            },
        ]
        self.payments: list[dict[str, Any]] = [
            {
                "id": 1,
                "project_id": 1,
                "project_name": "North Star Residence Renovation",
                "amount": 54000,
                "payment_date": str(today - timedelta(days=2)),
                "status": "received",
                "notes": "30% down payment",
            },
            {
                "id": 2,
                "project_id": 2,
                "project_name": "Central Park Apartment",
                "amount": 175000,
                "payment_date": str(today - timedelta(days=20)),
                "status": "received",
                "notes": "50% first installment",
            },
            {
                "id": 3,
                "project_id": 3,
                "project_name": "Harbor Loft",
                "amount": 336000,
                "payment_date": str(today - timedelta(days=10)),
                "status": "received",
                "notes": "80% milestone payment",
            },
        ]

    def list_items(self, collection: str) -> list[dict[str, Any]]:
        return deepcopy(getattr(self, collection))

    def add_item(self, collection: str, payload: dict[str, Any]) -> dict[str, Any]:
        item = {"id": next(self._counters[collection]), **payload}
        getattr(self, collection).append(item)
        return deepcopy(item)

    def update_item(self, collection: str, item_id: int, payload: dict[str, Any]) -> dict[str, Any] | None:
        items = getattr(self, collection)
        for index, item in enumerate(items):
            if item["id"] == item_id:
                updated = {**item, **payload, "id": item_id}
                items[index] = updated
                return deepcopy(updated)
        return None

    def project_cost_summary(self) -> list[dict[str, Any]]:
        summary = []
        for project in self.projects:
            procurement_total = sum(
                item["budget"] for item in self.procurements if item["project_id"] == project["id"]
            )
            payment_received = sum(
                item["amount"]
                for item in self.payments
                if item["project_id"] == project["id"] and item["status"] == "received"
            )
            gross_profit = project["budget"] - procurement_total
            gross_margin = round((gross_profit / project["budget"] * 100), 2) if project["budget"] > 0 else 0.0
            summary.append(
                {
                    "project_id": project["id"],
                    "project_name": project["project_name"],
                    "customer_name": project["customer_name"],
                    "budget": project["budget"],
                    "procurement_total": procurement_total,
                    "payment_received": payment_received,
                    "gross_profit": gross_profit,
                    "gross_margin": gross_margin,
                }
            )
        return summary

    def summary(self) -> dict[str, Any]:
        active_projects = [project for project in self.projects if project["progress"] < 100]
        procurement_budget = sum(item["budget"] for item in self.procurements)
        pending_inspections = sum(1 for item in self.inspections if item["result"] == "pending")
        avg_progress = round(sum(project["progress"] for project in self.projects) / len(self.projects))
        total_budget = sum(project["budget"] for project in self.projects)
        total_payments = sum(item["amount"] for item in self.payments if item["status"] == "received")
        total_procurement = sum(item["budget"] for item in self.procurements)
        total_gross_profit = total_budget - total_procurement
        overall_margin = round((total_gross_profit / total_budget * 100), 2) if total_budget > 0 else 0.0

        return {
            "generated_at": datetime.now().isoformat(timespec="seconds"),
            "metrics": [
                {"label": "Customer reports", "value": len(self.customers), "trend": "+3 this month"},
                {"label": "Measure bookings", "value": len(self.appointments), "trend": "2 upcoming"},
                {"label": "Active projects", "value": len(active_projects), "trend": f"{avg_progress}% avg progress"},
                {"label": "Pending inspections", "value": pending_inspections, "trend": "Quality follow-up"},
            ],
            "procurement_budget": procurement_budget,
            "financial_summary": {
                "total_budget": total_budget,
                "total_procurement": total_procurement,
                "total_payments_received": total_payments,
                "total_gross_profit": total_gross_profit,
                "overall_margin": overall_margin,
            },
            "project_costs": self.project_cost_summary(),
            "phase_distribution": [
                {"phase": phase, "count": sum(1 for project in self.projects if project["phase"] == phase)}
                for phase in sorted({project["phase"] for project in self.projects})
            ],
            "recent_updates": [
                {
                    "project_name": project["project_name"],
                    "phase": project["phase"],
                    "progress": project["progress"],
                    "latest_update": project["latest_update"],
                }
                for project in sorted(self.projects, key=lambda item: item["progress"], reverse=True)
            ],
        }


store = InMemoryStore()
