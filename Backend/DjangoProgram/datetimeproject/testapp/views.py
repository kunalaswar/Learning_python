from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def date_time_info(request):
    date = datetime.datetime.now()
    h = int(date.strftime("%H"))
    msg = "<h1>Hello guest, very "
    if h < 12:
        msg += "Good Morning"
    elif h < 16:
        msg += "Good Afternoon"
    elif h < 21:
        msg += "Good Evening"
    else:
        msg += "Good Night"
    
    msg += "!</h1><hr>"  # Properly closing the tag

    # Append the server time to the message 
    msg += f"<h1>Now the Server time is: {date}</h1>"

    return HttpResponse(msg)

