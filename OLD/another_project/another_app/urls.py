from django.urls import re_path
from another_app import views

urlpatterns = [
    re_path(r'^$', views.index, name="index"),
]