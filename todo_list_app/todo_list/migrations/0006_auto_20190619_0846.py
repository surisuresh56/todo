# Generated by Django 2.1.5 on 2019-06-19 08:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0005_auto_20190619_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='todo_task_dates_times',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 19, 8, 46, 0, 370571, tzinfo=utc)),
        ),
    ]