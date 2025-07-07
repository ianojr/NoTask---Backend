from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^tasks/$', views.Tasks_Api),
    re_path(r'^tasks/(?P<id>\d+)/$', views.Tasks_Api),
]
