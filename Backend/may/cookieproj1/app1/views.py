from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(request):
    name = request.GET.get('name') #this will read the details 
    link= '<a href=/find> Find My Name</a>'
    response = HttpResponse(link)
    response.set_cookie('name',name) # here key is name and value is also name 
    return response

# view2  should identity the request is come from which Client
def view2(request): # information is in request 
    # syntax :
    name=request.COOKIES.get('name')
    return HttpResponse('your name is :---  > '+name)


def home(request):
    response =render(request,'home.html',context={})
    return response 
