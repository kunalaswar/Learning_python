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


