from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcome_view(request):
    print("this line Add by View function ")
    return HttpResponse('<h1> Custumer MiddleWare</h1>')

