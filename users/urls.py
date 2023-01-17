from django.urls import path, include
from users import views

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'users_home'),
]
