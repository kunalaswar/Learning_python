from django.shortcuts import render
from testapp.forms import StudentForm
# Create your views here.
def Student_input_view(request):
    form  = StudentForm()
    if request.method =="post":
        form  = StudentForm(request.POST)
        if form.is_valid():
            print("Form Validation success and print data")
            print('Rollno:',form.cleaned_data['rollno'])
            print('Name:',form.cleaned_data['name'])
            print('Marks:',form.cleaned_data['marks'])
            submitted = True



    return render(request,template_name='testapp/input.html',context={'form':form,'submitted':submitted,'sname':'name'})


