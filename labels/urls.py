from django.urls import path, include
from labels import views

urlpatterns = [
    path('', views.LabelsView.as_view(), name = 'labels_home'),
]