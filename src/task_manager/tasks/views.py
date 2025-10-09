from django.http import JsonResponse

from tasks.models import Task


def get_task_details(request, task_id):
    task = get_task(task_id)
    if not task:
        return JsonResponse({"error": "Task not found"}, status=404)
    return JsonResponse(
        {
            "task": task.title,
            "description": task.description,
            "cost": task.cost,
            "completed": task.completed,
            "created_at": task.created_at,
            "updated_at": task.updated_at,
        }
    )
