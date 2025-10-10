from core.repositories import BaseRepository
from django.db import models
from executors.models import UserExecutor


class TaskManager(models.Manager):
    def get_by_id_from_repository(self, repository: BaseRepository, task_id: int):
        return repository[task_id]


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    cost = models.IntegerField(default=1)
    assignee = models.ForeignKey(
        UserExecutor, null=True, on_delete=models.SET_NULL, related_name="tasks"
    )
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = TaskManager()


class Dependency(models.Model):
    task = models.ForeignKey(
        Task, related_name="dependencies", on_delete=models.CASCADE
    )
    depends_on = models.ForeignKey(
        Task, related_name="dependents", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("task", "depends_on")
