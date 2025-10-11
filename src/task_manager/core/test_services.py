import pytest
from core.services import assign_task_to_executor
from django.contrib.auth.models import User
from executors.models import UserExecutor
from notifications.models import Notification
from profiles.models import Profile
from tasks.models import Task
from tasks.signal_receivers import handle_task_assigned


@pytest.mark.django_db
def test_assign_task_to_executor():
    user = User.objects.create_user(
        email="testuser@example.com", username="testuser", password="password"
    )
    profile = Profile.objects.create(user=user)
    executor = UserExecutor.objects.create(profile=profile)
    task = Task.objects.create(title="Test Task", description="A task for testing")
    assign_task_to_executor(task.id)
    task.refresh_from_db()
    assert task.assignee == executor
    notification = Notification.objects.filter(
        recipient=executor.profile.user.email
    ).first()
    assert notification is not None
    assert notification.message == f"Task '{task.title}' has been assigned to you."
