from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def info_view(request):
    subjects = {'s1':'python','s2':'Django','s3':'REST_API'}
    return render(request,'testapp/result.html',subjects)
