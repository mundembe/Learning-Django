from django.urls import re_path
from AppTwo import views

urlpatterns = [
    re_path(r'^help/', views.view_one, name="view_one"),
    re_path(r'contact/', views.view_two, name="contact"),

]