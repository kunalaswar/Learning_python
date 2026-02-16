from django.shortcuts import render
import datetime,random
# Create your views here.
def result_view(request):
    msg_list = [
        'The Golden days ahead',
        'Better to sleep more time even in classroom',
        'Tomorrow will be the best day of your life',
        'Tomorrow is the perfect day to purpose your GF',
        'Very soon you will get job',
    ]
    name_list = ['sunny','radhika','lily','katrina','kareena','Deepika','Samantha']
    time = datetime.datetime.now()
    h = int(time.strftime('%H'))
    if h <= 12:
        s = 'Good Morning'

    elif  h < 16:
        s = 'Good Afternoon'
    elif h < 21:
        s = 'Good Evening'    
    else:
        s = "Good Night"    
    name = random.choice(name_list)    
    msg = random.choice(msg_list)
    my_dict ={'time':time,"name":name,'msg': msg,'wish':s}
    return render(request,template_name="testapp/astrology.html",context=my_dict)


  