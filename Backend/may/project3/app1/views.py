from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    output = '''<HTML> <body bgcolor = cyan>
    <h1>INDEX PAGE</h1>
    </body>
    </HTML>'''
    response=HttpResponse(output)
    return response

def products(request):
    output='''<HTML>
    <BODY BGCOLOR=YELLOW>
    <H1>PRODUCT PAGE</H1>
    </BODY> </HTML>'''

    response=HttpResponse(output)
    return response

