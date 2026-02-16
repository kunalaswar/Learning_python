from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
# Create your views here.

class TestView(View): # how to call class  ---> by defining URL 
    def get(self,request):
        res = HttpResponse("GET Request")
        return res 

    def post(self,request):
        res=HttpResponse("POST Request")
        return res 

def display_temp(request):
    res = render(request,'test_temp.html',context={})
    return res 