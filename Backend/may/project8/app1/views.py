from django.shortcuts import render
#todo - rendering is nothing is but Including HTML code with Context Value 
# Create your views here.
def index(request):
    response = render(request,"index.html",context={})
    return response