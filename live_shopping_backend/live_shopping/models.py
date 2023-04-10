# live_shopping/models.py
from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class LiveVideoRequest(models.Model):
    """This class store the user's request for a live video session with a support person."""
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    DONE = "DONE"
    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (ACTIVE, "Active"),
        (DONE, "Done"),
    ]
    user_email = models.EmailField()
    user_name = models.CharField(max_length=128)
    user_dyte_participant_id = models.UUIDField(unique=True)
    dyte_meeting_id = models.UUIDField(unique=True)
    support_user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING, null=True)
    support_user_dyte_participant_id = models.UUIDField(null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    feedback = models.TextField()
    product = models.JSONField()