from django.contrib import admin
from todo_list.models import TodoList
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(TodoList)
class TodoListAdmin(ImportExportModelAdmin):
    list_display = ('title', 'description',
                    'todo_task_dates_times', 'status', 'created_at',
                    'modified_at',)
    list_filter = ('title', 'description', 'todo_task_dates_times', 'status', 'created_at',
                   'modified_at',)
    search_fields = ('title', 'description', 'todo_task_dates_times', 'status', 'created_at',
                     'modified_at',)
    ordering = ('todo_task_dates_times',)
