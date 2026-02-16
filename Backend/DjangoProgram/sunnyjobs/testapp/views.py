from django.shortcuts import render

from testapp.models import HydJobs 
# Create your views here.
def Home_page_views(request):
    return render(request,template_name='testapp/index.html')

def hydjobs_views(request):
    jobs_list = HydJobs.objects.all()   
    my_dict = {'jobs_list':jobs_list}
    return render(request,template_name = "testapp/hydjobs.html",context=my_dict)

