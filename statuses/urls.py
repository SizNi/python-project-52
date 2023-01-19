from django.urls import path, include
from statuses import views

urlpatterns = [
    path('', views.StatusesView.as_view(), name = 'statuses_home'),
    path('create/', views.CreateStatusesView.as_view(), name = 'create_status'),
    
]
