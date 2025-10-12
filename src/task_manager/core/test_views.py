import pytest
from core.services import assign_task_to_executor
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse
from executors.models import UserExecutor
from notifications.models import Notification
from profiles.models import Profile
from tasks.models import Task


@pytest.mark.django_db
def test_assign_task_view():
    user = User.objects.create_user(
        email="testuser@example.com", username="testuser", password="password"
    )
    profile = Profile.objects.create(user=user)
    executor = UserExecutor.objects.create(profile=profile)
    task = Task.objects.create(title="Test Task", description="A task for testing")
    client = Client()
    response = client.get(reverse("assign_task", args=[1]))
    assert response.status_code == 200
    assert response.json() == {"status": "Task assigned successfully."}
    task.refresh_from_db()
    assert task.assignee == executor
    notification = Notification.objects.filter(
        recipient=executor.profile.user.email
    ).first()
    assert notification is not None
    assert notification.message == f"Task '{task.title}' has been assigned to you."
