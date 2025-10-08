"""
Tests for the work action context boundary.
"""

from domain.work_action import models, services


def test_add_notes():
    agent = models.Agent(agent_id="a1")
    work_item = models.WorkItem(work_item_id="wi1", title="Work Item 1", assignee=agent)
    _ = models.WorkItem(
        work_item_id="wi1",
        title="Work Item 1",
        assignee=agent,
    )
    result = services.add_notes(agent, work_item, notes="Too easy.")
    assert result.notes == "Too easy."


def test_complete_work_item():
    agent = models.Agent(agent_id="a1")
    work_item = models.WorkItem(work_item_id="wi1", title="Work Item 1", assignee=agent)
    result = services.complete_work_item(agent, work_item)
    assert result.is_completed is True

