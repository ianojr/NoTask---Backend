from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^notes/$', views.Notes_Api),
    re_path(r'^notes/(?P<id>\d+)/$', views.Notes_Api),
]
