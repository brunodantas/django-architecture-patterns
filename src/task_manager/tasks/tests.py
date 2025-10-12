import pytest
from django.test import Client
from django.urls import reverse

from tasks.models import Task
from tasks.signal_receivers import fetch_task_details


@pytest.mark.django_db
def test_view_task_details():
    task = Task.objects.create(title="Sample Task", description="Too easy")
    client = Client()
    response = client.get(reverse("task_details", args=[task.id]))
    assert response.status_code == 200
    assert response.json() == {
        "id": task.id,
        "title": "Sample Task",
        "description": "Too easy",
        "completed": False,
    }
