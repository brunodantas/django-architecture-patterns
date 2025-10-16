from django.http import JsonResponse

from tasks.repositories import TaskRepository


def get_task_details(request, task_id):
    try:
        task = TaskRepository()[task_id]
        return JsonResponse(
            {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "completed": task.completed,
            }
        )
    except KeyError:
        return JsonResponse({"error": "Task not found"}, status=404)
