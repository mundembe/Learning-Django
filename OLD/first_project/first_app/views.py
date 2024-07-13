from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    my_variables = {"var1" : "Place the image below",}
    return render(request, 'first_app/index.html', context=my_variables)