from django.db import models
from django.contrib.auth.models import User
from submissions.models import Submission


class Upload(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    submission = models.ForeignKey(
        Submission,
        on_delete=models.CASCADE,
        related_name='submissionuploads'
        )
    upload = models.FileField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
