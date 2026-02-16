from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display (request):
    # s = "Hello Welcome to my first Django application"
    s = '<h1>Hello Welcome to my first Django application </h1>'
    return HttpResponse(s)
  