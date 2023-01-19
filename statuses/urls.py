from django.urls import path, include
from users import views

urlpatterns = [
    path('', views.StatusesView.as_view(), name = 'statuses_home'),
]
