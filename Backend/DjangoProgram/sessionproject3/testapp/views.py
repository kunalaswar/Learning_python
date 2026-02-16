from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request,'testapp/home.html')

def age_view(request):
    print(request.COOKIES)
    name = request.GET['name'] # this is a python basic aahe he  
    response = render(request,'testapp/age.html',{'name':name})
    response.set_cookie('name',name,3*30*24*60*60)
    return response


def gf_view(request):
    print(request.COOKIES)
    name = request.COOKIES['name']
    # how to read age 
    age = request.GET.get('age')
    response = render(request,'testapp/gf.html',{'name':name})
    response.set_cookie('age',age,120)
    return response

def result_view(request):
    print(request.COOKIES)
    name = request.COOKIES['name']
    age = request.COOKIES['age']
    gf = request.GET['gf']
    return render(request,'testapp/results.html',{'name':name,'age':age,'gf':gf})



