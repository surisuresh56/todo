from import_export import resources
from todo_list.models import TodoList

#'''added a module to get the table as excel sheets in django'''

class TodoListDataResource(resources.ModelResource):
    class Meta:
        model = TodoList
