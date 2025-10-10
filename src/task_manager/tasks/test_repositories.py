from tasks.models import Task
from tasks.repositories import DummyTaskRepository


def test_repository():
    repo = DummyTaskRepository()
    repo.insert(Task(id=1, title="Task 1", description="Desc"))
    assert len(repo) == 1
    assert 1 in repo
    task = repo[1]
    assert task.title == "Task 1"
    assert task.description == "Desc"
    assert task.cost == 1
    assert list(repo)[0].id == 1
