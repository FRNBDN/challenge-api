# Generated by Django 3.2.18 on 2023-03-14 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0014_group_members'),
        ('challenges', '0003_remove_challenge_criteria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.group'),
        ),
    ]