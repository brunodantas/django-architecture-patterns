from django.db import models

from executors.models import UserExecutor


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

    def __str__(self):
        return f"{self.title} (Cost: {self.cost}, Completed: {self.completed})"


class Dependency(models.Model):
    task = models.ForeignKey(
        Task, related_name="dependencies", on_delete=models.CASCADE
    )
    depends_on = models.ForeignKey(
        Task, related_name="dependents", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("task", "depends_on")
