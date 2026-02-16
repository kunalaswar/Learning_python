from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    s = "<h1>This is second app that is testapp</h1>"
    return HttpResponse(s)
