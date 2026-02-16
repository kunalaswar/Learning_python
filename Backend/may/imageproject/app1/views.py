from django.shortcuts import render,redirect
from app1.forms import PersonForm
from app1.models import Person
# Create your views here.
def addview(request):
    #^ if request method is POST Execute this logic 
    if request.method == "POST":
        # print("hello") # only for debugging purpose
        f = PersonForm(request.POST,request.FILES)# we have to put file here 
        if f.is_valid():
            f.save()
            response = redirect('personlist')
            return response 
            # after saving it again i want to display Empty form 
    # This is a Empty form 
    #^ if request method is GET Execute this logic 
    form = PersonForm()    
    response = render(request,"person_temp.html",context={'form':form}) 
    return response

def person_list(request):
    qs = Person.objects.all() # Person.moduleManager.all()
    response = render(request,'personlist_temp.html',context={'qs':qs})
    return response



