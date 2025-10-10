import random


class Task:
    def __init__(self, task_id, title, description, cost, completed, assignee):
        self.id = task_id
        self.title = title
        self.description = description
        self.cost = cost
        self.completed = completed
        self.assignee = assignee

    def assign_task(self, executors):
        """Assigns a task to a random executor from the list."""
        if not executors:
            raise ValueError("No executors available for scheduling.")
        if self.completed:
            raise ValueError("Cannot schedule a completed task.")
        assignee = random.choice(executors)
        self.assignee = assignee
