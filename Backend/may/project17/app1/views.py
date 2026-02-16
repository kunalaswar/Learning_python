from django.shortcuts import render,redirect
from app1.forms import EmpForm
from app1.forms import EmpModel 
# Create your views here.
def addemp_view(request): #* this view hendle 2 request Get & post 
    if request.method=="POST":
        form=EmpForm(request.POST)
        if form.is_valid():
            form.save()
            # res=render(request,'listemp.html',context={})
            #^ Here one view call another view  using one function redirect()
            res=redirect('listemp')
            return res    
        else:
            res=render(request,'addemp.html',context={'form':form})    
            return res

    form=EmpForm()
    res=render(request,'addemp.html',context={'form':form})
    return res

def listemp_view(request):
    qs=EmpModel.objects.all()
    res=render(request,'listemp.html',context={'qs':qs})
    return res

def update_view(request,eno): #^ when you click on link this is GET request 
    emp=EmpModel.objects.get(empno=eno) 
    if request.method=="POST": #^khalachi line for request.post update data is parat save karaysathi
        form=EmpForm(request.POST,instance=emp )
        form.save()
        res=redirect("listemp") #^ 
        return res
        #^ if request method is GET if cha else part 
    
        # form=EmpForm(instance=emp) #* we can store Employee detail by writing instance 
    form=EmpForm(instance=emp)
        
    res=render(request,"updateemp.html",context={"form":form})
    return res
def delete_view(request,eno):#!below line first read the details of employee then i want conformation you want ot delete or not
    emp=EmpModel.objects.get(empno=eno) #EmpModel.modelmanager
    if request.method=="POST":
        emp.delete()
        res=redirect('listemp')
        return res 

    form=EmpForm(instance=emp)
    res=render(request,"confirm.html",context={'emp':emp})
    return res 