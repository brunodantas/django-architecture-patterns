"""
Mock repositories for testing.
"""

from domain.work_action import models
from domain.work_action.repositories import BaseWorkItemRepository


class MockWorkItemRepository(BaseWorkItemRepository):
    def __init__(self):
        self.storage = {}

    def save(self, work_item: models.WorkItem) -> None:
        self.storage[work_item.work_item_id] = work_item

    def get_by_id(self, work_item_id: str) -> models.WorkItem | None:
        return self.storage.get(work_item_id)
