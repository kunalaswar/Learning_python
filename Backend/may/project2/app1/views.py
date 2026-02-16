from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def deposit(request):
    msg = "<h2> Deposit view</h2>"
    output = HttpResponse(msg)
    return output

def withdraw(request):
    msg = "<h2> Withdraw view</h2>"
    output = HttpResponse(msg)
    return output

