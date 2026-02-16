from django.shortcuts import render

# Create your views here.
#^ here we have to create a one login view 
def loginview(request):
    if request.method=='POST':
        user = request.POST.get("user")
        request.session['user'] = user # key = value session contain key and value 
        response = render(request,'inbox.html',context={'user':user})
        return response
    response = render(request,'login.html')
    return response
