# Generated by Django 2.1.5 on 2019-06-20 06:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0007_auto_20190619_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created_at',
            field=models.DateField(default='2019-06-20'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='modified_at',
            field=models.DateField(default='2019-06-20'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='status',
            field=models.CharField(choices=[('Inprogress', 'Inprogress'), ('Completed', 'Completed'), ('Pending', 'Pending')], max_length=1),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='todo_task_dates_times',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 20, 6, 14, 19, 760514, tzinfo=utc)),
        ),
    ]
