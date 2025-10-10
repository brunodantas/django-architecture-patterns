from django.db import models
from executors.models import UserExecutor

from tasks.domain.task import Task as DomainTask


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    cost = models.IntegerField(default=1)
    completed = models.BooleanField(default=False)
    assignee = models.ForeignKey(
        UserExecutor, null=True, on_delete=models.SET_NULL, related_name="tasks"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_domain(self) -> DomainTask:
        return DomainTask(
            task_id=self.id,
            title=self.title,
            description=self.description,
            cost=self.cost,
            completed=self.completed,
            assignee=self.assignee,
        )

    @classmethod
    def from_domain(cls, domain_task: DomainTask) -> "Task":
        instance = cls()
        instance.title = domain_task.title
        instance.description = domain_task.description
        instance.cost = domain_task.cost
        instance.completed = domain_task.completed
        instance.assignee = domain_task.assignee
        return instance


class Dependency(models.Model):
    task = models.ForeignKey(
        Task, related_name="dependencies", on_delete=models.CASCADE
    )
    depends_on = models.ForeignKey(
        Task, related_name="dependents", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("task", "depends_on")
