import pytest
from core import models

from domain.work_action import models as domain_models
from domain.work_action import services
from work_action import repositories


@pytest.mark.django_db
def test_work_item_repository_add_notes():
    agent_repository = repositories.DjangoAgentRepository()
    agent = domain_models.Agent(agent_id="agent1")
    agent_repository.save(agent)
    work_item = domain_models.WorkItem(
        work_item_id="1", title="Test Work Item", assignee=agent
    )
    repository = repositories.DjangoWorkItemRepository()
    repository.save(work_item)
    services.add_notes(agent, work_item, "Too easy.", repository)
    retrieved = models.WorkItem.objects.first()
    assert retrieved is not None
    assert retrieved.notes == "Too easy."


@pytest.mark.django_db
def test_complete_work_item():
    agent_repository = repositories.DjangoAgentRepository()
    agent = domain_models.Agent(agent_id="agent1")
    agent_repository.save(agent)
    work_item = domain_models.WorkItem(
        work_item_id="1", title="Test Work Item", assignee=agent
    )
    repository = repositories.DjangoWorkItemRepository()
    repository.save(work_item)
    services.complete_work_item(agent, work_item, repository)
    retrieved = models.WorkItem.objects.first()
    assert retrieved is not None
    assert retrieved.is_completed is True
