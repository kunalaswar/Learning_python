from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def welcome (request):
    msg = "<h2>Welcome to Django 01-10-2025</h2>"
    output = HttpResponse(msg)
    return output