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

    def __str__(self) -> str:
        return self.name or self.email

    def __repr__(self) -> str:
        return f"User(user_id={self.user_id}, email={self.email}, name={self.name})"


@dataclass
class Manager:
    """
    Represents a manager who performs CRUD
    on users and work items.
    """

    manager_id: str
    user: User

    def __str__(self) -> str:
        return str(self.user)

    def __repr__(self) -> str:
        return f"Manager(manager_id={self.manager_id}, user={self.user})"


@dataclass
class AutomatedAgent:
    """
    Represents an automated agent that acts on work items.
    """

    automated_agent_id: str
    agent_id: str
    created_by: Manager
    name: str = ""

    def __str__(self) -> str:
        return self.name or self.agent_id

    def __repr__(self) -> str:
        return f"AutomatedAgent(automated_agent_id={self.automated_agent_id}, agent_id={self.agent_id}, created_by={self.created_by}, name={self.name})"


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

    def __str__(self) -> str:
        if self.user:
            return str(self.user)
        if self.automated_agent:
            return str(self.automated_agent)
        return f"Agent(agent_id={self.agent_id})"

    def __repr__(self) -> str:
        return f"Agent(agent_id={self.agent_id}, user={self.user}, automated_agent={self.automated_agent}, team_id={self.team_id})"


@dataclass
class Team:
    """
    Represents a team of agents.
    """

    team_id: str
    name: str
    created_by: Manager
    agents: list[Agent] = field(default_factory=list)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Team(team_id={self.team_id}, name={self.name}, created_by={self.created_by}, agents={self.agents})"


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

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f"WorkItem(work_item_id={self.work_item_id}, title={self.title}, created_by={self.created_by}, notes={self.notes}, assignee={self.assignee}, is_completed={self.is_completed})"


@dataclass
class Project:
    """
    Represents a project that contains work items.
    """

    project_id: str
    name: str
    created_by: Manager
    work_items: list[WorkItem] = field(default_factory=list)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Project(project_id={self.project_id}, name={self.name}, created_by={self.created_by}, work_items={self.work_items})"


@dataclass
class Dependency:
    """
    Represents a dependency between two work items.
    """

    from_work_item: WorkItem
    to_work_item: WorkItem

    def __str__(self) -> str:
        return f"{self.from_work_item} -> {self.to_work_item}"

    def __repr__(self) -> str:
        return f"Dependency(from_work_item={self.from_work_item}, to_work_item={self.to_work_item})"
