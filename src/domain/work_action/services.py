"""
Services for the work action context boundary.
"""

from domain.work_action import models


def add_notes(
    agent: models.Agent, work_item: models.WorkItem, notes: str
) -> models.WorkItem:
    """
    Adds notes to a work item.
    """
    if not isinstance(agent, models.Agent):
        raise ValueError("Only agents can add notes.")
    if agent != work_item.assignee:
        raise ValueError("Only the assignee can add notes.")
    if not isinstance(work_item, models.WorkItem):
        raise ValueError("The work_item parameter must be a WorkItem instance.")
    if not isinstance(notes, str) or not notes:
        raise ValueError("Notes must be a non-empty string.")
    work_item.notes = notes
    return work_item


def complete_work_item(
    agent: models.Agent, work_item: models.WorkItem
) -> models.WorkItem:
    """
    Marks a work item as completed.
    """
    if not isinstance(work_item, models.WorkItem):
        raise ValueError("The work_item parameter must be a WorkItem instance.")
    if not isinstance(agent, models.Agent):
        raise ValueError("Only agents can complete work items.")
    if agent != work_item.assignee:
        raise ValueError("Only the assignee can complete the work item.")
    if any(not dependency.is_completed for dependency in work_item.dependencies):
        raise ValueError(
            "All dependencies must be completed before completing this work item."
        )
    work_item.is_completed = True
    return work_item
