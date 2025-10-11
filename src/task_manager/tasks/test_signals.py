import pytest

from tasks.models import Task


@pytest.mark.django_db
def test_updated_at_signal():
    task = Task.objects.create(title="Test Task", description="A task for testing")
    original_updated_at = task.updated_at

    task.title = "Updated Test Task"
    task.save()

    assert task.updated_at > original_updated_at
