from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


CATEGORY_CHOICES = (
    ('SPI', 'Spiritual'),
    ('FIN', 'Financial'),
    ('CAR', 'Career'),
    ('INT', 'Intellectual'),
    ('FIT', 'Fitness'),
    ('SOC', 'Social'),
    ('ETC', 'Other'),
)


class Group(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=160, unique=True, blank=False)
    category = models.CharField(max_length=25,
                                choices=CATEGORY_CHOICES,
                                default='ETC')
    tags = TaggableManager(blank=True)
    members = models.ManyToManyField(User, related_name='members')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f" ({self.id}) [{self.category}] {self.title}"
