from django.shortcuts import render,redirect
from todo_list.models import TodoList
from rest_framework import viewsets
from todo_list.serializers import TodoListSerializer
# Create your views here.

def index(request):
    todos = TodoList.objects.all()
    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["title"]
            description = request.POST["description"]
            todo_task_dates_times = request.POST["todo_task_dates_times"]
            status = request.POST["status"]
            created_at = request.POST["created_at"]
            modified_at = request.POST["modified_at"]
            Todo = TodoList(title=title, description=description, todo_task_dates_times=todo_task_dates_times, status=status,created_at=created_at,modified_at=modified_at)
            Todo.save()
            return redirect("/")
        if "taskDelete" in request.POST:
            checkedlist = request.POST["checkedbox"]
            todo = TodoList.objects.get(id=int(checkedlist))
            todo.delete()

    return render(request, "index.html", {"todos": todos})

class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer