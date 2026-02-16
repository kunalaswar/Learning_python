from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(request):
    output = "<h1>View1 of Application1</h1>"
    res =  HttpResponse(output)
    return res 

def view2(request):
    output = "<h1>View2 of Application1</h1>"
    res = HttpResponse(output)
    return res 

#todo -  Copy app1 of project4 inside project5 (copy/paste)
# 1. Create project 
# django-admin startproject project5
# 2. Copy app1 of project4 inside project5 (copy/paste)
# 3. Open project5  urls.py
