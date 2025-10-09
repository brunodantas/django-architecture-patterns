from domain.work_action import models, repositories
from core import models as web_models


class DjangoWorkItemRepository(repositories.BaseWorkItemRepository):
    def save(self, work_item: models.WorkItem) -> None:
        web_work_item = web_models.WorkItem.from_domain_model(work_item)
        if saved_instance := web_models.WorkItem.objects.filter(
            work_item_id=work_item.work_item_id
        ).first():
            web_work_item.id = saved_instance.id
        web_work_item.save()


class DjangoAgentRepository:
    def save(self, agent: models.Agent) -> None:
        web_agent = web_models.Agent.from_domain_model(agent)
        web_agent.save()
