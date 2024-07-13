from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {"django_code": "this is from django code"}
    return render(request, "first_app/index.html", context=my_dict)