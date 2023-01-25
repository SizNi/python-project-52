from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.TasksView.as_view(), name='tasks_home'),
    path('create/', views.TasksCreateView.as_view(), name='task_create'),
    path(
        '<int:pk>/update/',
        views.TasksUpdateView.as_view(),
        name='task_update'
    ),
    path(
        '<int:pk>/delete/',
        views.TasksDeleteView.as_view(),
        name='task_delete'
    ),
    path('<int:pk>/', views.TaskView.as_view(), name='task'),
]
