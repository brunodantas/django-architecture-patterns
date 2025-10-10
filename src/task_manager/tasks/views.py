from django.http import JsonResponse

from tasks.services import assign_task_to_executor


def asssign_task(task_id: int):
    try:
        assign_task_to_executor(task_id)
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"message": "Task assigned successfully."})
