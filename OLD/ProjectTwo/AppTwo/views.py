from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def view_one(request):
    my_variables = {
        "my_template_var" : "Help Page",
        "other_var": "this is the other var", 
        
    }
    return render(request, "help/help.html", context=my_variables)

def view_two(request):
    my_dict = {
        "phone" : "068 283 0059"
    }
    return render(request, "contact/contact.html", context=my_dict)