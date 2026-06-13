from app.services.base import CrudService
from app.data.store import store


class ProjectService(CrudService):
    collection = "projects"

    def cost_summary(self) -> list[dict]:
        return store.project_cost_summary()


project_service = ProjectService()
