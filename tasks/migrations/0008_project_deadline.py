# Generated by Django 3.0.2 on 2020-10-18 09:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_remove_project_dedline'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='deadline',
            field=models.DateField(default=datetime.date.today, verbose_name='Deadline of the project (year, month, day)'),
        ),
    ]