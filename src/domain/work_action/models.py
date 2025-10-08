"""
Models for the work action context boundary.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """
    Represents an agent who acts on work items.
    Can be a user or an automated agent.
    """

    agent_id: str

    def __str__(self) -> str:
        return self.agent_id

    def __repr__(self) -> str:
        return f"Agent(agent_id={self.agent_id})"


@dataclass
class WorkItem:
    """
    Represents a work item that can be assigned to agents.
    """

    work_item_id: str
    title: str
    notes: str = ""
    assignee: Agent | None = None
    is_completed: bool = False
    dependencies: List["WorkItem"] = field(default_factory=list)

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f"WorkItem(work_item_id={self.work_item_id}, title={self.title}, notes={self.notes}, assignee={self.assignee}, is_completed={self.is_completed})"
