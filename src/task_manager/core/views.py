from django.http import JsonResponse

from core.signals import assign_task


def assign_task_view(request, task_id):
    try:
        assign_task.send_robust(sender=assign_task_view, task_id=task_id)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"status": "Task assigned successfully."})
