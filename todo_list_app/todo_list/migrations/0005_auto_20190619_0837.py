# Generated by Django 2.1.5 on 2019-06-19 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0004_auto_20190619_0835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='todotask_datetime',
            new_name='todo_task_dates_times',
        ),
    ]