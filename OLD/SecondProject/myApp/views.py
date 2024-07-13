from django.shortcuts import render

# Create your views here.
def home(request):
    my_vars = {
        "my_text" : "This is text injected from django",
    }
    return render(request, "home/index.html", context=my_vars)