from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def view1(request):
    output = '''<h1>Views1 of Application2</h1>'''
    res = HttpResponse(output)
    return res

def view2(request):
    output = '''<h1>Views2 of Application2</h1>'''
    res = HttpResponse(output)
    return res
