from django.shortcuts import render

# Create your views here.

from django.db.models import Avg,Max,Min,Sum,Count
def aggregate_view(request):
    avg = Employee.objects.all().aggregate(Avg('esal'))
    max = Employee.objects.all().aggregate(Max('esal'))
    min = Employee.objects.all().aggregate(Min('esal'))
    sum = Employee.objects.all().aggregate(Sum('esal'))
    count = Employee.objects.all().aggregate(Count('esal'))
    my_dict = {'avg':avg['esal__avg'], 'max':max['esal__max'], 'min':min['esal__min'], 'sum':sum['esal__sum'],'count':count['esal__count']}
    return render(request,'testapp/aggregate.html',my_dict)

from testapp.models import Employee
# def retrieve_view(request):
    # emp_list = Employee.objects.all()
    # emp_list = Employee.objects.filter(esal__gt = 15000) # greter than 
    # emp_list = Employee.objects.filter(esal__gte = 15000)# greter than or equal to 
    # print(type(emp_list))
    # emp_list = Employee.objects.filter(ename__contains='Jeffrey Lee')
    # emp_list = Employee.objects.filter(ename__contains='Jo')
    # emp_list = Employee.objects.filter(id__in=[1,3,5])
    # emp_list = Employee.objects.filter(ename__startswith='s') 
    # emp_list = Employee.objects.filter(ename__endswith='s') 
    # emp_list = Employee.objects.filter(esal__range=[12000,15000]) 
    # emp_list = Employee.objects.filter(ename__endswith='s')|Employee.objects.filter(esal__lt=180000) # this is OR 
    # from django.db.models import Q
    # emp_list = Employee.objects.filter(Q(ename__startswith='A') | Q(esal__lt=13000))
    # emp_list = Employee.objects.filter(ename__startswith='S') & Employee.objects.filter(esal__lt=15000)
    # emp_list = Employee.objects.filter(Q(ename__startswith='A') & Q(esal__lt=18000))
    # emp_list = Employee.objects.filter(ename__startswith='A',esal__lt=18000)
    #todo - Ex:To select all employees whose name not starts with 'S'
    # emp_list = Employee.objects.exclude(ename__startswith='S')
    # emp_list = Employee.objects.filter(~Q(ename__startswith='S'))
    #todo- How to select only required columns in the query set?
    # emp_list = Employee.objects.all().values_list('ename','esal')
    #^ 2) by using values() data is in form of dict 
    # emp_list = Employee.objects.all().values('ename','esal')
    #^ 2) by using only() data is in form of objects
    # emp_list = Employee.objects.all().only('ename','esal')

    # print(emp_list)
    # return render(request,'testapp/specificcolumn.html',{'emp_list':emp_list})

from django.db.models.functions import Lower 
def retrieve_view(request):
    #todo Django Middleware 
    #*------------------------------------
    print(request.user) #todo -  kunal    AuthenticationMiddleware 
    #*------------------------------------
    # How to perform union operation for query set?
    # q1 = Employee.objects.filter(esal__lt=12000)
    # q2 = Employee.objects.filter(ename__startswith='s')
    # emp_list = q1.union(q2)
    # emp_list = Employee.objects.all().order_by(Lower('ename')) # Lower 
    # emp_list = Employee.objects.all().order_by('eno') # forward
    # emp_list = Employee.objects.all().order_by('-eno') # reverse
    emp_list = Employee.objects.all().order_by('ename') 
    print(emp_list)   
    return render(request,'testapp/index.html',{'emp_list':emp_list})
    
    # return render(request,'testapp/index.html',{'emp_list':emp_list})
   
#Similarly we can use __lt and __lte also.

    # print(type(emp_list))
	# <class 'django.db.models.query.QuerySet'>


# Q.To get higest salaried employee?
# Arrange all employees in descending order and select first employee.
# >>> e = Employee.objects.all().order_by('-esal')[0]
# >>> e.ename
# >>> e.esal    



# this from chatgpt 
# Q(ename__startswith='A')
# Q = Query object (allows complex conditions)
# ename__startswith = field lookup (name starts with)
# 'A' = the letter to check