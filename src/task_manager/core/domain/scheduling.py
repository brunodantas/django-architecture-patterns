import random
from typing import List

from executors.models import UserExecutor
from tasks.models import Task


def assign_task(task: Task, executors: List[UserExecutor]):
    """Assigns a task to a random executor from the list."""
    if not executors:
        raise ValueError("No executors available for scheduling.")
    if task.completed:
        raise ValueError("Cannot schedule a completed task.")
    assignee = random.choice(executors)
    task.assignee = assignee
    task.save()
