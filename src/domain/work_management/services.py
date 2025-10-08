"""
Services for the work management context boundary.
"""

from uuid import uuid4

from domain.work_management import models


def create_user(
    email: str, name: str = "", roles: list[str] = ["agent"]
) -> models.User:
    """
    Creates a new user.
    """
    # TODO: add check for unique email
    is_agent = "agent" in roles
    is_manager = "manager" in roles
    if not is_agent and not is_manager:
        raise ValueError("User must have at least one valid role.")
    user_id = str(uuid4())
    user = models.User(user_id=user_id, email=email, name=name)

    # TODO: persist agent/manager
    if is_agent:
        _ = models.Agent(agent_id=str(uuid4()), user=user)
    if is_manager:
        _ = models.Manager(manager_id=str(uuid4()), user=user)
    return user


def create_work_item(
    work_item_id: str,
    title: str,
    created_by: models.Manager,
) -> models.WorkItem:
    """
    Creates a new work item.
    """
    if not isinstance(created_by, models.Manager):
        raise ValueError("Only managers can create work items.")
    return models.WorkItem(
        work_item_id=work_item_id,
        title=title,
        created_by=created_by,
    )


def create_automated_agent(
    automated_agent_id: str,
    created_by: models.Manager,
) -> models.AutomatedAgent:
    """
    Creates a new automated agent.
    """
    if not isinstance(created_by, models.Manager):
        raise ValueError("Only managers can create automated agents.")
    return models.AutomatedAgent(
        automated_agent_id=automated_agent_id,
        agent_id=str(uuid4()),
        created_by=created_by,
    )


def link_work_items(
    from_work_item: models.WorkItem,
    to_work_item: models.WorkItem,
    created_by: models.Manager,
) -> models.Dependency:
    """
    Links two work items as a dependency.
    """
    if not isinstance(created_by, models.Manager):
        raise ValueError("Only managers can link work items.")
    if not isinstance(from_work_item, models.WorkItem) or not isinstance(
        to_work_item, models.WorkItem
    ):
        raise ValueError("The parameters must be WorkItem instances.")
    return models.Dependency(
        from_work_item=from_work_item,
        to_work_item=to_work_item,
    )


def assign_work_item(
    assigner: models.Manager,
    work_item: models.WorkItem,
    assignee: models.Agent,
) -> models.WorkItem:
    """
    Assigns a work item to an agent.
    """
    if not isinstance(assigner, models.Manager):
        raise ValueError("Only managers can assign work items.")
    work_item.assignee = assignee
    return work_item
