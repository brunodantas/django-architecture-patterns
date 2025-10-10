from django.db import transaction
from executors.models import UserExecutor
from tasks.models import Task


def create_task_for_executor(executor_id: int):
    with transaction.atomic():
        task = Task.objects.create(title="New Task", description="Auto-created task")
        executor = UserExecutor.objects.get(id=executor_id)
        task.assignee = executor
        task.save()
    return task
