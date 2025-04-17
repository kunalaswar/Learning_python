from django.shortcuts import render
from testapp.models import Employees
# Create your views here.
def emp_data_view(request):
    emp_list = Employees.objects.all() # select * from Emoloyees
    my_dict = {'emp_list':emp_list}
    return render (request,template_name='testapp/emp.html',context = my_dict)

