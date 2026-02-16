from django.shortcuts import render

# Create your views here.
def index(request):
    response = render(request,"app1/index.html")
    return response

def courses(request):
    response = render(request,"app1/courses.html")
    return response

def about(request):
    response = render(request,"app1/about.html")
    return response

def contacts(request):
    response = render(request,"app1/contacts.html")
    return response

