from django.shortcuts import render
import datetime
# Create your views here.
def info_view(request):
    time = datetime.datetime.now()
    name = "Django"
    prerequisite = 'python'
    my_dict = {'time':time,'name':name,'prerequisite':prerequisite}
    return render(request,template_name='testapp/results.html',context=my_dict)  # context is the opitional

