import pytest
from tasks.models import Task
from tasks.repositories import DummyTaskRepository, TaskRepository


@pytest.mark.django_db
def test_dummy_repository():
    repo = DummyTaskRepository()
    repo.insert(Task(id=1, title="Task 1", description="Desc"))
    assert len(repo) == 1
    assert 1 in repo
    task = repo[1]
    assert task.title == "Task 1"
    assert task.description == "Desc"
    assert task.cost == 1
    assert list(repo)[0].id == 1


@pytest.mark.django_db
def test_queryset_repository():
    repo = TaskRepository()
    repo.insert(Task(id=1, title="Task 1", description="Desc"))
    assert len(repo) == 1
    assert 1 in repo
    task = repo[1]
    assert task.title == "Task 1"
    assert task.description == "Desc"
    assert task.cost == 1
    assert list(repo)[0].id == 1
