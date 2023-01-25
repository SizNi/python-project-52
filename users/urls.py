from django.urls import path
from users import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='users_home'),
    path(
        '<int:pk>/update/',
        views.UserUpdateView.as_view(),
        name='update_user'
    ),
    path(
        '<int:pk>/delete/',
        views.UserDeleteView.as_view(),
        name='delete_user'
    ),
    path('create/', views.CreateView.as_view(), name='create_user'),
]
