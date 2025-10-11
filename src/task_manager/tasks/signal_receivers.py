from django.db.models import signals
from django.dispatch import receiver
from django.utils import timezone
from notifications.models import Notification

from tasks.models import Task
from tasks.signals import task_assigned


@receiver(signals.pre_save, sender=Task)
def handle_pre_save(sender, instance, *args, **kwargs):
    instance.updated_at = timezone.now()


@receiver(task_assigned)
def handle_task_assigned(sender, task, **kwargs):
    recipient = task.assignee.profile.user.email
    Notification.objects.create(
        message=f"Task '{task.title}' has been assigned to you.",
        recipient=recipient,
    )
