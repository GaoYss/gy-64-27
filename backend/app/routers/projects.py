from fastapi import APIRouter

from app.schemas.projects import Project, ProjectCreate, ProjectUpdate, ProjectCostSummary
from app.services.projects import project_service

router = APIRouter(prefix="/api/projects", tags=["projects"])


@router.get("", response_model=list[Project])
def list_projects() -> list[dict]:
    return project_service.list()


@router.get("/cost-summary", response_model=list[ProjectCostSummary])
def get_project_cost_summary() -> list[dict]:
    return project_service.cost_summary()


@router.post("", response_model=Project, status_code=201)
def create_project(payload: ProjectCreate) -> dict:
    return project_service.create(payload)


@router.patch("/{project_id}", response_model=Project)
def update_project(project_id: int, payload: ProjectUpdate) -> dict:
    return project_service.update(project_id, payload)
