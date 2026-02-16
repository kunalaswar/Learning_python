from django.shortcuts import render
from app1.forms import RegisterForm
from django.http import HttpResponse
# Create your views here.

def register_view(request):#^ request is HTTPRequest object 
    if request.method=="GET":
        form=RegisterForm()
        response = render(request,'register.html',context={'form':form})
        return response 
    elif request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['uname']
            # prinf'{name} Registered')
            output =f'<h1>{name} is registered</h1>'
            res=HttpResponse(output)
            return res
        else:
            res=render(request,"register.html",context={'form':form})
            return res
        

