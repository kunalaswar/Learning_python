from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_view(request):
    return HttpResponse("<h1> first view Response</h1>")
def second_view(request):
    return HttpResponse("<h1> second view Response</h1>")
def third_view(request):
    return HttpResponse("<h1> third view Response</h1>")

