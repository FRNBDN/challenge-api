# Generated by Django 3.2.18 on 2023-03-10 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0012_group_challenge_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='challenge_title',
        ),
        migrations.RemoveField(
            model_name='group',
            name='criteria',
        ),
        migrations.RemoveField(
            model_name='group',
            name='date',
        ),
        migrations.RemoveField(
            model_name='group',
            name='description',
        ),
        migrations.RemoveField(
            model_name='group',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='group',
            name='repetition',
        ),
    ]
