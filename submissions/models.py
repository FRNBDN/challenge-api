from django.db import models
from django.contrib.auth.models import User
from groups.models import Group
from challenges.models import Challenge

SUBMISSION_STATUS = (
    (1, 'Submitted'),
    (2, 'Completed'),
    (3, 'Failed'),
)


class Submission(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    challenge = models.OneToOneField(Challenge, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    stauts = models.CharField(
        max_length=50,
        choices=SUBMISSION_STATUS,
        default=1)
