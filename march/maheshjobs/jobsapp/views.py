from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hyd_jobs_info(request):
    s = "<h1>Hyberabad jobs information </h1>"
    return HttpResponse(s)
def bng_jobs_info(request):
    s = "<h1>Bangalore jobs information </h1>"
    return HttpResponse(s)
def pune_jobs_info(request):
    s = "<h1>pune jobs information</h1>"
    return HttpResponse(s)
def noida_jobs_info(request):
    s ="<h1>noida jobs information</h1>"
    return HttpResponse(s)



