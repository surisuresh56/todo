from rest_framework import serializers
from todo_list.models import TodoList

class TodoListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TodoList
        fields = ('id', 'title', 'description', 'todo_task_dates_times', 'status', 'created_at', 'modified_at')