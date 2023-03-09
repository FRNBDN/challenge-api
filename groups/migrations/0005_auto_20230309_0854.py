# Generated by Django 3.2.18 on 2023-03-09 08:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_auto_20230308_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='category',
            field=models.CharField(choices=[('SPI', 'Spiritual'), ('FIN', 'Financial'), ('CAR', 'Career'), ('INT', 'Intellectual'), ('FIT', 'Fitness'), ('SOC', 'Social'), ('ETC', 'Other')], default='ETC', max_length=25),
        ),
        migrations.AlterField(
            model_name='group',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='group',
            name='repetition',
            field=models.CharField(choices=[('never', 'One Time Challenge'), ('daily', 'Repeats Daily'), ('weekly', 'Repeats Weekly'), ('monthly', 'Repeats Monthly'), ('annualy', 'Repeats Annualy')], default='weekly', max_length=25),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=160, unique=True),
        ),
    ]