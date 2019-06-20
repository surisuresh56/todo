# Generated by Django 2.1.5 on 2019-06-19 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('Description', models.TextField(blank=True)),
                ('todotask_datetime', models.DateTimeField(default='2019-06-19 07:16:34')),
                ('Status', models.CharField(choices=[('Inprogress', 'Inprogress'), ('Completed', 'Completed'), ('Pending', 'Pending')], max_length=1)),
                ('Created_at', models.DateField(default='2019-06-19')),
                ('Modified_at', models.DateField(default='2019-06-19')),
            ],
            options={
                'ordering': ['-todotask_datetime'],
            },
        ),
    ]
