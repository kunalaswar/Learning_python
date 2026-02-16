from django.shortcuts import render
from testapp.models import Employee
# Create your views here.
def display_view(request):
    # return type of the emp_list is Queryset 
    emp_list = Employee.objects.all() # <class 'django.db.models.manager.Manager'>
    return render(request,'testapp/index.html',{'emp_list':emp_list})

