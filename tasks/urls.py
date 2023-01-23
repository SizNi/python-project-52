from django.urls import path, include
from tasks import views

urlpatterns = [
    path('', views.TasksView.as_view(), name = 'tasks_home'),
    path('create/', views.TasksCreateView.as_view(), name = 'task_create'),
]