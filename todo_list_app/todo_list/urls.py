from django.conf.urls import url
from django.urls import include, path
from todo_list import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'todo', views.TodoListViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('', include(router.urls)),
    ]