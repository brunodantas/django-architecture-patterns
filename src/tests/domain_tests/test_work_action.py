"""
Tests for the work action context boundary.
"""

from domain.work_action import models, services
from tests.repositories import MockWorkItemRepository


def test_add_notes():
    agent = models.Agent(agent_id="a1")
    work_item = models.WorkItem(work_item_id="wi1", title="Work Item 1", assignee=agent)
    repository = MockWorkItemRepository()
    repository.save(work_item)
    services.add_notes(
        agent, work_item, notes="Too easy.", work_item_repository=repository
    )
    updated_work_item = repository.get_by_id("wi1")
    assert updated_work_item is not None
    assert updated_work_item.notes == "Too easy."


def test_complete_work_item():
    agent = models.Agent(agent_id="a1")
    work_item = models.WorkItem(work_item_id="wi1", title="Work Item 1", assignee=agent)
    repository = MockWorkItemRepository()
    repository.save(work_item)
    services.complete_work_item(agent, work_item, repository)
    updated_work_item = repository.get_by_id("wi1")
    assert updated_work_item is not None
    assert updated_work_item.is_completed is True
