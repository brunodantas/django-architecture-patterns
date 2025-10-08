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
