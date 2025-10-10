import pytest
from core.services import create_task_for_executor
from executors.models import UserExecutor
from tasks.models import Task


@pytest.mark.django_db
def test_create_task_for_executor_fails(db, django_user_model):
    with pytest.raises(UserExecutor.DoesNotExist):
        create_task_for_executor(executor_id=123456)
    # Check no task was created
    assert Task.objects.count() == 0
