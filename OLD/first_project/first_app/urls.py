from django.urls import re_path, include
from first_app import views

urlpatterns = [
    re_path(r'^$', views.home, name="home"),
]
