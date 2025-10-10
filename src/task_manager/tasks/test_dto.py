from tasks.dto import SchedulingDTO


def test_scheduling_dto_from_dict():
    data = {
        "assignments": [
            {"executor_id": 1, "task_ids": [1, 2]},
            {"executor_id": 2, "task_ids": [3]},
        ],
        "tasks": [
            {"task_id": 1, "title": "Task 1", "start_day": 0, "end_day": 2},
            {"task_id": 2, "title": "Task 2", "start_day": 3, "end_day": 5},
        ],
    }
    dto = SchedulingDTO.from_dict(data)
    assert len(dto.assignments) == 2
    assert dto.assignments[0].executor_id == 1
    assert dto.assignments[0].task_ids == [1, 2]
    assert dto.assignments[1].executor_id == 2
    assert dto.assignments[1].task_ids == [3]
    assert len(dto.schedule) == 2
    assert dto.schedule[0].task_id == 1
    assert dto.schedule[0].title == "Task 1"
    assert dto.schedule[0].start_day == 0
    assert dto.schedule[0].end_day == 2
    assert dto.schedule[1].task_id == 2
    assert dto.schedule[1].title == "Task 2"
    assert dto.schedule[1].start_day == 3
    assert dto.schedule[1].end_day == 5
