from core.repositories import BaseRepository

from tasks.models import Task


class TaskRepository(BaseRepository):
    def __init__(self, queryset=None) -> None:
        super().__init__(queryset or Task.objects.all())


class DummyTaskRepository(TaskRepository):
    def __init__(self, queryset=None) -> None:
        """Init with a custom queryset"""
        self.base_queryset = {}

    def __len__(self):
        return len(self.base_queryset)

    def __iter__(self):
        for task in self.base_queryset.values():
            yield task

    def __contains__(self, key):
        return key in self.base_queryset

    def __getitem__(self, key):
        try:
            return self.base_queryset[key]
        except KeyError:
            raise KeyError("Task not found")

    def insert(self, item):
        self.base_queryset[item.id] = item
