from django.urls import re_path
from myApp import views

urlpatterns = [
    re_path(r'$', views.home, name="home"),
]