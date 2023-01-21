from django.contrib import admin
from django.urls import path, include
from task_manager import views

urlpatterns = [
    path('', views.Index.as_view(), name = 'home'),
    path('users/', include('users.urls')),
    path('statuses/', include('statuses.urls')),
    path('tasks/', include('tasks.urls')),
    path('login/', views.LoginView.as_view(), name = 'login'),
    path('logout/', views.LogoutView.as_view(), name = 'logout'),
    path('admin/', admin.site.urls),
]
