from django.urls import re_path
from . import views

urlpatterns = [
    # Tasks endpoints
    re_path(r'^tasks/$', views.Tags_Api),
    re_path(r'^tasks/(?P<id>\d+)/$', views.Tags_Api),

    # Tags endpoints
    re_path(r'^tags/$', views.Tags_Api),
    re_path(r'^tags/(?P<id>\d+)/$', views.Tags_Api),

    # NoteTags endpoints
    re_path(r'^note-tags/$', views.NoteTags_Api),
    re_path(r'^note-tags/(?P<id>\d+)/$', views.NoteTags_Api),

    # TaskTags endpoints
    re_path(r'^task-tags/$', views.TaskTags_Api),
    re_path(r'^task-tags/(?P<id>\d+)/$', views.TaskTags_Api),

    # NoteTasks endpoints
    re_path(r'^note-tasks/$', views.NoteTasks_Api),
    re_path(r'^note-tasks/(?P<id>\d+)/$', views.NoteTasks_Api),
]
