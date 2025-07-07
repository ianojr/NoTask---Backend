from django.contrib import admin
from django.urls import path
from users.views import (
    RegisterView, UserListView, UserDetailView, UserUpdateView, UserDeleteView, login_api
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Registration and login
    path('users/register/', RegisterView.as_view(), name='register'),
    path('users/login/', login_api, name='login'),

    # User CRUD
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
]