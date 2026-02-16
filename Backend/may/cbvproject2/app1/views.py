from django.shortcuts import render
from app1.forms import EmpForm
from django.views import View  #todo - Beacuse i am creating classbase view 
from app1.models import EmpModel
from django.views.generic import ListView
# Create your views here.
# view name is EmpCreateView 
class EmpCreateView(View):
    def get(self,request):
        form = EmpForm() #^ I am Creating one Empty form with the help of EmpForm Class 
        res = render(request,"emp_create.html",context={'form':form})
        return res 
    def post(self,request):
        form = EmpForm(request.POST) #^ we have to populate it 
        if form.is_valid():
            form.save()
            #^ Again we required Empty form
            form = EmpForm()
            # res = render(request,'')
            res = render(request,"emp_create.html",context={'form':form, 'msg':'Employee created'})
            return res 
        else:
            res = render(request,"emp_create.html",context={'form':form})
            return res 
        
class EmpListView(ListView):
    # def get(self,request):
    #     qs = EmpModel.objects.all()
    #     res = render(request,'emp_list.html',context={'qs':qs})
    #     return res 
    #todo- we not defined in side of view just defined property
    model = EmpModel 
#1. model = EmpModel
# This tells Django:
# “Please take all the data from the EmpModel table.”
#^ Same as writing:
# qs = EmpModel.objects.all()
    template_name = 'emp_list.html'
# 2. template_name = 'emp_list.html'
# This tells Django:
# “Use this HTML file to show the data.”
#^ Without this line, Django would look for a file named:
# app1/empmodel_list.html    
    context_object_name ='emp'
#     3. context_object_name = 'emp'
# This tells Django:
# “Send the list of employees to the template using the variable name emp.”
#^ Meaning inside your HTML you will use:


#^ if it is Department list  here is only Model and .html is changes 
# class DeptList(View):
#     def get(self,request):
#         qs = DeptModel.objects.all()
#         res = render(request,'dept_list.html',context={'qs':qs})
#         return res 
