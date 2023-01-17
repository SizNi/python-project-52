from django.contrib import admin
from django.urls import path, include
from task_manager import views

urlpatterns = [
    path('', views.Index.as_view(), name = 'home'),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]
