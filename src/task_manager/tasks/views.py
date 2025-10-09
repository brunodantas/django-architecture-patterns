from django.http import JsonResponse

from tasks.models import Task


def get_task_details(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        return JsonResponse(
            {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "completed": task.completed,
            }
        )
    except Task.DoesNotExist:
        return JsonResponse({"error": "Task not found"}, status=404)
