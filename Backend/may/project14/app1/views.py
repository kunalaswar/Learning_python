from django.shortcuts import render

# Create your views here.
def view1(request):
    rollno = 1
    name = "naresh"
    course = "python"
    stud = {"rollno":rollno,"name":name,"course":course}
    res = render(request,'dtl.html',context= {"stud":stud})
    return res

def view2(request):
    a= 10
    b= 20
    response = render(request,'dtl2.html',context={'a':a,'b':b})
    return response

def view3(request):
    name = 'naresh'
    avg = 60
    res = render(request,'dtl3.html',context={'name':name,'avg':avg})
    return res

def view4(request):
    email_list=['kunal@gmail.com',
                'harshal@gmail.com',
                'aniket@gmail.com']
    res = render(request,'dtl4.html',context={'email_list':email_list})
    return res
def view5(request):
    marks = {'naresh':[40,50,60],
            'ramesh':[60,70,80],
            'suresh':[70,80,90]}
    res = render(request,'dtl5.html',context={'marks':marks})
    return res

def view6(request):
    A = [10,20,30,40,50]
    res = render(request,'dtl6.html',context={'A':A})
    return res 

def view7(request):
    res = render(request,"child1.html",context={})
    return res

def view8(request):
    res = render(request,"child2.html",context={})
    return res



