from django.db import models

from profiles.models import Profile


class Executor(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserExecutor(Executor):
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name="executor"
    )
