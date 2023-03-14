# Generated by Django 3.2.18 on 2023-03-14 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0002_delete_uploads'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='stauts',
            field=models.CharField(choices=[(1, 'Submitted'), (2, 'Completed'), (3, 'Failed')], default=1, max_length=50),
        ),
    ]