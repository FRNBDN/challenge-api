# Generated by Django 3.2.18 on 2023-03-13 12:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('submissions', '0002_delete_uploads'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('owner', 'submission')},
        ),
    ]
