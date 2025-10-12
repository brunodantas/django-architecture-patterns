import random

from core.signals import assign_task
from django.dispatch import receiver
from executors.models import UserExecutor
from tasks.models import Task
from tasks.signals import task_assigned


def get_available_executors():
    busy_executors = Task.objects.filter(completed=False).values_list(
        "assignee_id", flat=True
    )
    return UserExecutor.objects.exclude(id__in=list(busy_executors))


@receiver(assign_task)
def assign_task_to_executor(sender, task_id: int, **kwargs):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        raise ValueError("Task not found.")
    if task.assignee is not None:
        raise ValueError("Task is already assigned.")
    executors = get_available_executors()
    if not executors:
        raise ValueError("No executors available.")
    task.assignee = random.choice(executors)
    task.save()
    task_assigned.send(sender=assign_task_to_executor, task=task)
