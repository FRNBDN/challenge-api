from django.db import models
from django.contrib.auth.models import User
from groups.models import Group
from challenges.models import Challenge


class Submission(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    challenge = models.OneToOneField(Challenge, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)


class Uploads(models.Model):
    submission = models.ForeignKey(Submission,
                                   on_delete=models.CASCADE,
                                   related_name='submissionuploads')
    upload = models.FileField(upload_to='uploads/', blank=True, null=True)
