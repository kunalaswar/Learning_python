from django.shortcuts import render,redirect
from testapp.models import Employee
# Create your views here.
def retrieve_view(request):
    emp_list = Employee.objects.all()
    return render(request,'testapp/index.html',{'emp_list':emp_list})

from testapp.forms import EmployeeForm

def insert_view(request):   
    form  =EmployeeForm() # this is Create a Empty Form  #^ form is black here 
    # for submit the data  we have to save it 
    if request.method =='POST': # current object method 
        form = EmployeeForm(request.POST) #^ toch variable pointing to fill data this form is pointing to user provided data
        if form.is_valid():
            form.save()
        return redirect('/') # this line is always run it form is valid or not and redirst to the home page 
    return render(request,'testapp/insert.html',{'form':form})


def delete_view(request,id):
    employee = Employee.objects.get(id=id) # .get(id=id) = finding the employee whose id matches
    employee.delete()
    return redirect('/')   

# def update_view(request,id):
#     employee = Employee.objects.get(id=id)
#     form = EmployeeForm(instance=employee) # this means that this form is display the current Employee details it contain current Employee Details 
#     return render(request,'testapp/update.html',{'form':form})


def update_view(request,id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(instance=employee) # instance=employee fills the form with current values
    if request.method == 'POST': 
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():                   
            form.save()
        return redirect('/')
    return render(request,'testapp/update.html',{'form':form})

