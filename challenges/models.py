from django.db import models
from django.contrib.auth.models import User
from groups.models import Group


class Challenge(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=160)
    number = models.CharField(max_length=16)
    date = models.DateField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} #{self.number}"
