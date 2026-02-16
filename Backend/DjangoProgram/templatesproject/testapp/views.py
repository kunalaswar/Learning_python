from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def display(request):
    date = datetime.datetime.now()
    msg = "Hello guest very good"
    h = int(date.strftime('%H'))
    if h <= 12:
        msg += "Morinng"
    elif h < 16:
        msg += "Afternoon"    
    elif h < 21:
        msg +="Evening"    
    else:
        msg += "Night"    



    my_dict = {'insert_date':date}
    # name = "Kunal"   
    # marks= 89
    # rollno= 101
    # my_dict = {'insert_date':date,'name':name,'marks':marks,'rollno':rollno}
    
    return render(request,template_name='testapp/wish.html',context=my_dict) # here context= is send data to templates 