from django.db import models
from django.contrib.auth.models import User
from groups.models import Group


class Member(models.Model):
    member = models.ForeignKey(
        User, related_name='member', on_delete=models.CASCADE
    )
    group = models.ForeignKey(
        Group, related_name='group', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['member', 'group']

    def __str__(self):
        return f'{self.member} {self.group}'
