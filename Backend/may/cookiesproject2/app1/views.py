from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    response = render(request,"home.html",context={})
    return response

def users(request):
    response = render(request,"user.html",context={})
    return response

def newuser(request):
    name = request.POST.get('user') # here reading the user name 
    output = f'''<h2>hello {name} </h2>
             <h2><a href="/home">Home</a></h2> '''
    response = HttpResponse('<h2>Hello '+  name+'</h2>')
    response.set_cookie(key='name',value=name,max_age=7*24*60*60) #todo-cookies contain key and value this is an Persistant cookies so that it contain the two para Extra max_age=7day*24hours*60Minute*60Seconds and Expiry  
    return response

def existinguser(request):
    name = request.COOKIES.get("name") # abd your reading the the value of name 
    output = "Hello"+name+"Welcome back"
    response = HttpResponse(output)
    return response


