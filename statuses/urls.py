from django.urls import path
from statuses import views

urlpatterns = [
    path('', views.StatusesView.as_view(), name='statuses_home'),
    path(
        'create/',
        views.CreateStatusesView.as_view(),
        name='create_status'
    ),
    path(
        '<int:pk>/update/',
        views.UpdateStatusesView.as_view(),
        name='update_status'
    ),
    path(
        '<int:pk>/delete/',
        views.DeleteStatusView.as_view(),
        name='delete_status'
    ),

]
