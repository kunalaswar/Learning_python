from django.shortcuts import render
from app1.forms import StudentForm
from django.http import HttpResponse
# Create your views here.
flag=True
def student_view(request):
    global flag
    if flag:            
        studform=StudentForm()
        response=render(request,'student_temp.html',context={'studform':studform})
        flag=False
        return response
    else:
        # response=HttpResponse("<h2>Response</h2>")
        # studform = StudentForm(request.GET)
        # studform = StudentForm(rollno=request.GET.get('rollno'),name= request.GET.get('name'),course=request.GET.get('course'))
        studform = StudentForm(request.GET)
        if studform.is_valid():
            rollno=studform.cleaned_data['rollno']
            name = studform.cleaned_data['name']
            course = studform.cleaned_data['course']
            print(rollno,name,course)
            # flag=True
        studform=StudentForm()
        response=render(request,"student_temp.html",context={'studform':studform })
        return response