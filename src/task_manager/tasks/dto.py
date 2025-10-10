class TaskAssignmentDTO:
    def __init__(self, executor_id: int, task_ids: list[int]):
        self.executor_id = executor_id
        self.task_ids = task_ids

    @classmethod
    def from_dict(cls, data: dict) -> "TaskAssignmentDTO":
        return cls(
            executor_id=data.get("executor_id", -1),
            task_ids=data.get("task_ids", []),
        )


class TaskScheduleDTO:
    def __init__(self, task_id: int, title: str, start_day: int, end_day: int):
        self.task_id = task_id
        self.title = title
        self.start_day = start_day
        self.end_day = end_day

    @classmethod
    def from_dict(cls, data: dict) -> "TaskScheduleDTO":
        return cls(
            task_id=data.get("task_id", -1),
            title=data.get("title", ""),
            start_day=data.get("start_day", -1),
            end_day=data.get("end_day", -1),
        )


class SchedulingDTO:
    def __init__(
        self,
        assignments: list[TaskAssignmentDTO],
        schedule: list[TaskScheduleDTO],
    ):
        self.assignments = assignments
        self.schedule = schedule

    @classmethod
    def from_dict(cls, data: dict) -> "SchedulingDTO":
        assignments = [
            TaskAssignmentDTO.from_dict(item) for item in data.get("assignments", [])
        ]
        schedule = [TaskScheduleDTO.from_dict(item) for item in data.get("tasks", [])]
        return cls(assignments=assignments, schedule=schedule)
