from django.urls import path

from core.views import assign_task_view

urlpatterns = [
    path("assign-task/<int:task_id>/", assign_task_view, name="assign_task"),
]
