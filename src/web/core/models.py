from django.db import models

from domain.work_action import models as domain_models


class Agent(models.Model):
    agent_id = models.CharField(max_length=36, unique=True)

    @classmethod
    def from_domain_model(cls, domain_model: domain_models.Agent):
        agent = cls(agent_id=domain_model.agent_id)
        return agent


class WorkItem(models.Model):
    work_item_id = models.CharField(max_length=36, unique=True)
    title = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    assignee = models.ForeignKey(Agent, null=True, on_delete=models.SET_NULL)
    is_completed = models.BooleanField(default=False)

    @classmethod
    def from_domain_model(cls, domain_model: domain_models.WorkItem):
        work_item = cls(
            work_item_id=domain_model.work_item_id,
            title=domain_model.title,
            notes=domain_model.notes,
            assignee=Agent.objects.get(agent_id=domain_model.assignee.agent_id)
            if domain_model.assignee
            else None,
            is_completed=domain_model.is_completed,
        )
        return work_item


class Dependency(models.Model):
    from_work_item = models.ForeignKey(
        WorkItem, related_name="from_work_items", on_delete=models.CASCADE
    )
    to_work_item = models.ForeignKey(
        WorkItem, related_name="to_work_items", on_delete=models.CASCADE
    )
