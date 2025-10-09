from django.urls import path

from tasks import views

urlpatterns = [
    path("/<int:task_id>/", views.get_task_details, name="task_details"),
]
