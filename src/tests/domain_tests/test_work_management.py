"""
Tests for work management services.
"""

from domain.work_management import models, services


def test_create_user():
    user = services.create_user(email="user1@example.com", name="User One")
    assert user.email == "user1@example.com"
    assert user.name == "User One"


def test_create_work_item():
    manager = models.Manager(
        manager_id="m1",
        user=models.User(
            user_id="u1", email="manager1@example.com", name="Manager One"
        ),
    )
    work_item = services.create_work_item(
        work_item_id="wi1", title="Work Item 1", created_by=manager
    )
    assert work_item.work_item_id == "wi1"
    assert work_item.title == "Work Item 1"
    assert work_item.created_by == manager


def test_create_automated_agent():
    manager = models.Manager(
        manager_id="m1",
        user=models.User(
            user_id="u1", email="manager1@example.com", name="Manager One"
        ),
    )
    automated_agent = services.create_automated_agent(
        automated_agent_id="aa1", created_by=manager
    )
    assert automated_agent.automated_agent_id == "aa1"
    assert automated_agent.created_by == manager


def test_link_work_items():
    manager = models.Manager(
        manager_id="m1",
        user=models.User(
            user_id="u1", email="manager1@example.com", name="Manager One"
        ),
    )
    work_item1 = services.create_work_item(
        work_item_id="wi1", title="Work Item 1", created_by=manager
    )
    work_item2 = services.create_work_item(
        work_item_id="wi2", title="Work Item 2", created_by=manager
    )
    dependency = services.link_work_items(
        from_work_item=work_item1,
        to_work_item=work_item2,
        created_by=manager,
    )
    assert dependency.from_work_item == work_item1
    assert dependency.to_work_item == work_item2


def test_assign_work_item():
    agent = models.Agent(
        agent_id="a1",
        user=models.User(user_id="u2", email="agent1@example.com", name="Agent One"),
    )
    manager = models.Manager(
        manager_id="m1",
        user=models.User(
            user_id="u1", email="manager1@example.com", name="Manager One"
        ),
    )
    work_item = services.create_work_item(
        work_item_id="wi1", title="Work Item 1", created_by=manager
    )
    work_item.assignee = agent
    assert work_item.assignee == agent
