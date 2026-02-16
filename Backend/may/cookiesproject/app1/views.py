from django.shortcuts import render
# from django.views import View #^ this is Class Based View OK
from app1.forms import ProductForm
# Create your views here.
def addproduct(request): # Each view receive a request manun aapan parameter madhe request lehat
    if request.method=="POST": #todo- here you are reading the post Details that are send by Client 
        name = request.POST.get('name')#todo- what are the request you are reaing 
        qty=request.POST.get('qty') 
        # you have to add to the cookies
        res= render(request,'home.html',context={}) # we have to add with response
        res.set_cookie(name,qty)# Every cookies is identity by cookies 
        return res
    #^ if request method is get    
    form= ProductForm()
    # here we are adding the empty form to the addproduct_temp.html
    res = render(request,'addproduct_temp.html',context={'form':form})
    return res 

def home(request):
    res = render(request,'home.html',context={})
    return res 
        
def viewcart(request):
    products={}
    for name,qty in request.COOKIES.items(): # csrftoken  gamavaya sathi
        if name!= 'csrftoken':
            products[name]=qty
    res = render(request,'viewcart_temp.html',context={'products':products})
    # res = render(request,'viewcart_temp.html',context={'products':request.COOKIES})#^cookies is dictionary you can send to the viewcart_temp.html
    return res 

def updateproduct(request): #
    if request.method=="POST": #todo-
        name = request.POST.get('name')#todo-
        qty=request.POST.get('qty') 
        # you have to add to the cookies
        res= render(request,'home.html',context={}) #
        res.set_cookie(name,qty)#
        return res
    #^ if request method is get    
    form= ProductForm()
    res = render(request,'addproduct_temp.html',context={'form':form})
    return res 

def deleteproduct(request):
    if request.method=="POST": #todo-
        name = request.POST.get('name') 
        # qty=request.POST.get('qty')  # here when deleting we dont want Qty we can delete with the help of name
        # you have to add to the cookies
        res= render(request,'home.html',context={}) #
        res.delete_cookie(name)
        return res
    #^ if request method is get    
    form= ProductForm()
    res = render(request,'deleteproduct_temp.html',context={'form':form})
    return res 

