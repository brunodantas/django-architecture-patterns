"""
Models for the work action context boundary.
"""

from dataclasses import dataclass, field


@dataclass
class User:
    """
    Represents a user who can log into the system.
    Has unique email.
    """

    user_id: str
    email: str
    name: str = ""


@dataclass
class Manager:
    """
    Represents a manager who performs CRUD
    on users and work items.
    """

    manager_id: str
    user: User


@dataclass
class AutomatedAgent:
    """
    Represents an automated agent that acts on work items.
    """

    automated_agent_id: str
    agent_id: str
    created_by: Manager
    name: str = ""


@dataclass
class Agent:
    """
    Represents an agent who acts on work items.
    Can be a user or an automated agent.
    """

    agent_id: str
    user: User | None = None
    automated_agent: AutomatedAgent | None = None
    team_id: str | None = None


@dataclass
class Team:
    """
    Represents a team of agents.
    """

    team_id: str
    name: str
    created_by: Manager
    agents: list[Agent] = field(default_factory=list)


@dataclass
class WorkItem:
    """
    Represents a work item that can be acted upon.
    """

    work_item_id: str
    title: str
    created_by: Manager
    notes: str = ""
    assignee: Agent | None = None
    is_completed: bool = False


@dataclass
class Project:
    """
    Represents a project that contains work items.
    """

    project_id: str
    name: str
    created_by: Manager
    work_items: list[WorkItem] = field(default_factory=list)


@dataclass
class Dependency:
    """
    Represents a dependency between two work items.
    """

    from_work_item: WorkItem
    to_work_item: WorkItem
