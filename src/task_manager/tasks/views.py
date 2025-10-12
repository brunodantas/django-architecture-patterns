from django.http import JsonResponse

from tasks.signals import fetch_task_details


def get_task_details(request, task_id):
    result = fetch_task_details.send(sender=get_task_details, task_id=task_id)
    return JsonResponse(result[0][1])
