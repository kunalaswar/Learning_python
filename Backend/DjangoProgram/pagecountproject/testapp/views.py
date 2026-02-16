from django.shortcuts import render

# Create your views here.
def page_count_view(request):
    print("Cookies from Client:",request.COOKIES) # dict aahe he (Cookies from Client: {'count': '26'})
    count= int(request.COOKIES.get('count',0))
    count =count+1
    response =  render(request,'testapp/count.html',{'count':count})
    # ithon vegada aahe direct response nahi send karun rahalo user le with the help cookies pan pathaun rahalo 
    response.set_cookie('count',count) 
    return response


