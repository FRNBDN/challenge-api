from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from datetime import date

CATEGORY_CHOICES = (
    ('SPI', 'Spiritual'),
    ('FIN', 'Financial'),
    ('CAR', 'Career'),
    ('INT', 'Intellectual'),
    ('FIT', 'Fitness'),
    ('SOC', 'Social'),
    ('ETC', 'Other'),
)

REPETITION_CHOICES = (
    ('never', 'One Time Challenge'),
    ('daily', 'Repeats Daily'),
    ('weekly', 'Repeats Weekly'),
    ('monthly', 'Repeats Monthly'),
    ('annualy', 'Repeats Annualy'),
)


class Group(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=160, unique=True, blank=False)
    category = models.CharField(max_length=25,
                                choices=CATEGORY_CHOICES,
                                default='ETC')
    challenge_title = models.CharField(max_length=160, default="Challenge")
    description = models.TextField(max_length=500, default='...')
    criteria = models.TextField(max_length=500, default='...')
    date = models.DateField(default=date.today, blank=False)
    repetition = models.CharField(
        max_length=25, choices=REPETITION_CHOICES, default='weekly')
    end_date = models.DateField(blank=True, null=True)
    tags = TaggableManager(blank=True)
    # memebers and challenge missing

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"[{self.category}] {self.title} ({self.id})"
