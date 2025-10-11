from django.db import models


class Notification(models.Model):
    message = models.TextField()
    recipient = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    sent = models.BooleanField(default=False)
