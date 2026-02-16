from django.shortcuts import render
from app1.forms import *

# Create your views here.
def email_validator(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            res = render(request, "valid_temp.html", context={'msg': 'input data is valid'})
            return res
        else:
            res = render(request, "email_temp.html", context={'form': form})
            return res
    form = EmailForm()
    res = render(request, "email_temp.html", context={'form': form})
    return res
