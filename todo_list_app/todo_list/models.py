from django.db import models
from django.utils import timezone
# Create your models here.

class TodoList(models.Model):
    status_list = (
        ('Inprogress', 'Inprogress'),
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
    )
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    todo_task_dates_times = models.DateTimeField(default=timezone.now())
    status =models.CharField(max_length=1, choices=status_list)
    created_at = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    modified_at = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    def __str__(self):
        return self.title
