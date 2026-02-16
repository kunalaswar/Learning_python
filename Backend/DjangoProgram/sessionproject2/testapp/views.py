from django.shortcuts import render

from testapp.forms import LoginForm
# Create your views here.
def home_view(request):
    form = LoginForm()
    return render(request,'testapp/home.html',{'form':form})

def date_time_view(request):
    name = request.GET['name']
    response=render(request,'testapp/datetime.html',{'name':name})
    response.set_cookie('name',name)
    return response # response along with COOKIES 
import datetime
def result_view(request):
    name = request.COOKIES.get('name')

    date = datetime.datetime.now()
    return render(request,'testapp/result.html',{'name':name,'date':date})


