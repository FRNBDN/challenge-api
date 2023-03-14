from django.db import models
from django.contrib.auth.models import User
from datetime import date
from groups.models import Group


REPETITION_CHOICES = (
    ('never', 'One Time Challenge'),
    ('daily', 'Repeats Daily'),
    ('weekly', 'Repeats Weekly'),
    ('monthly', 'Repeats Monthly'),
    ('annualy', 'Repeats Annualy'),
)


class Challenge(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=160, default="Challenge")
    description = models.TextField(max_length=500, default='...')
    date = models.DateField(default=date.today, blank=False)
    repetition = models.CharField(
        max_length=25, choices=REPETITION_CHOICES, default='weekly')
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"({self.id}) {self.title}"
