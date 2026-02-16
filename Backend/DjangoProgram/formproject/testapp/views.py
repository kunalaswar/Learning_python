from django.shortcuts import render
from testapp.forms import StudentForm
# Create your views here.
def student_input_view(request):
    form_obj = StudentForm()
    my_dict = {'form_obj':form_obj}
    return render(request,template_name= 'testapp/input.html',context=my_dict)
