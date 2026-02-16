from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index (request):
    output = '''<html>
    <body bgcolor = cyan>
    <h1>INDEX PAGE</h1>
    </body>
    </html>'''
    response = HttpResponse(output)
    return response

def products(request):
    output = '''<html>
    <body bgcolor = yellow>
    <h1>PRODUCT PAGE</h1>
    </body></html>'''
    response = HttpResponse(output)
    return response
