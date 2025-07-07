from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^category/$', views.Category_Api),
    re_path(r'^category/(?P<id>\d+)/$', views.Category_Api),
]
