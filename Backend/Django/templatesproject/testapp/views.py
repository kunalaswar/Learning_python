from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def display(request):
    date = datetime.datetime.now()
    name = "Sunny"
    marks= 98
    rollno = 101
    my_dict = {'insert_date':date,'name':name,'marks':marks,'rollno':rollno}
    return render(request,template_name='testapp/wish.html',context=my_dict)


