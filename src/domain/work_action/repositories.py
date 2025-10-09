"""
Repositories for work action context boundary.
"""

from domain.work_action import models


class BaseWorkItemRepository:
    """
    Base repository interface for WorkItem.
    """

    def save(self, work_item) -> None:
        raise NotImplementedError

    def get_by_id(self, work_item_id: str) -> models.WorkItem | None:
        raise NotImplementedError
