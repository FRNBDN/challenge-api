from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

CATEGORY_CHOICES = (
    ('spiritual', 'SPIRITUAl'),
    ('financial', 'FINANCIAL'),
    ('career', 'CAREER'),
    ('intellectual', 'INTELLECTUAL'),
    ('fitness', 'FITNESS'),
    ('social', 'SOCIAL'),
)

REPETITION_CHOICES = (
    ('never', 'NEVER'),
    ('daily', 'DAILY'),
    ('weekly', 'WEEKLY'),
    ('monthly', 'MONTHLY'),
    ('annualy', 'ANNUALY'),
)


class Group(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=160)
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES)
    description = models.TextField(max_length=255)
    criteria = models.TextField()
    date = models.DateField()
    repetition = models.CharField(
        max_length=25, choices=REPETITION_CHOICES, default='never')
    tags = TaggableManager()
    # memebers and challenge missing

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.id} {self.title} {self.category}"
