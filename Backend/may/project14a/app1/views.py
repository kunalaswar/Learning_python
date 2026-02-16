from django.shortcuts import render

# Create your views here.
def view9(request):
    res = render(request,'base1.html',context={})
    return res
def view10(request):
    res = render(request,'child3.html',context={})

def view11(request):
    res = render(request,'')

def view12(request):
    res = render(request,'home.html',context={})
    return res
def view13(request):
    res = render(request,'courses.html',context={})
    return res
def view14(request):
    res = render(request,'calc.html',context={})
    return res

