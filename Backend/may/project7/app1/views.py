from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display(request,name,age):
    output = f'<h1>Name:{name} and Age {age} </h1>'
    response = HttpResponse(output)
    return response

