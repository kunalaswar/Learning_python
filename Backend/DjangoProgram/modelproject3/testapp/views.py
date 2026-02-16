from django.shortcuts import render
from testapp.models import student
# Create your views here.

def student_view(request):
    #student_list= student.objects.all()  #* moduleclass name.property. function()
    # student_list  = student.objects.filter(marks__lte = 35)  #* whose marks lessthan 35
    # student_list = student.objects.filter(name__startswith = 'A') #* whose name startwith 'A'
    # student_list = student.objects.all().order_by("marks")  #* group by marks ascending orderby bydefalut
    student_list = student.objects.all().order_by("-marks")   #* group by marks decending orderby set - sign 
    my_dict  ={"student_list":student_list}
    return render(request,template_name='testapp/std.html',context=my_dict)
