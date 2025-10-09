from task_manager.tasks.models import Task


def get_task(task_id: int) -> Task | None:
    try:
	    # Example additional business logic
		# Keep a last_accessed_by record
        return Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return None
