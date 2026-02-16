from django.shortcuts import render

from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponseRedirect

def home_page_view(request):
    return render(request,'testapp/home.html')        
def logout_view(request):
    return render(request,'testapp/logout.html')
#============signup ======================
from testapp.forms import SignUForm
def  signup_view(request):
    form = SignUForm() # create an object of that class EMPTY form aahe
    #! from barala nanter 
    if request.method == 'POST':
        form = SignUForm(request.POST) # data ghe
        user = form.save() # data save kar 
        user.set_password(user.password)#To hash password convert the hash password 
        user.save()   # once it convert then  save that password 
        return HttpResponseRedirect('/accounts/login/')
    return render(request,'testapp/signup.html',{'form':form})

@login_required 
def java_page_view(request):
    return render(request,'testapp/javaexam.html')
@login_required
def python_page_view(request):
    return render(request,'testapp/pythonexam.html')
@login_required
def aptitude_page_view(request):
    return render(request,'testapp/aptitudeexam.html')



