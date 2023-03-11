from django.db import models
from django.contrib.auth.models import User
from submissions.models import Submission


class Review(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.body