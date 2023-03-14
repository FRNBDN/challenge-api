from django.db import models
from django.contrib.auth.models import User
from challenges.models import Challenge


class Member(models.Model):
    member = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    challenge = models.ForeignKey(
        Challenge, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['member', 'challenge']

    def __str__(self):
        return f'{self.member} {self.challenge}'
