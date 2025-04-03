from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def time_info(request):
    date = datetime.datetime.now()
    msg = '<h1>Hello Friends Good Morning !!!</h1><hr>'
    msg += '<h2>Now Server time is: '+str(date)+ '</h2>'
    msg += '<h2>Now Server time is: '+repr(date)+ '</h2>'
    return HttpResponse(msg)




    