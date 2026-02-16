from django.shortcuts import render
from app1.forms import RegisterForm
# Create your views here.
flag=True #& this is GET request
def register_view(request): #todo this method handle two thing render the page and receiving data from form
    global flag
    if flag: #* this is for reading the data send by client
        form=RegisterForm() #todo- form is the object that have a data and put into the context to send form 
        res = render(request,'register.html',context={'form':form})
        
        flag=False
        return res
    else: #& this is POST request but both  are handle by GET request only 
        form=RegisterForm(request.GET) # if uppercondition false then the data is stored in request object senf to form 
        if form.is_valid(): # is_valid() method call clean method
            uname=form.cleaned_data['uname']
            print(f'{uname} Registeration Completed')
        else: #* registration form with data and along with Error   
            res = render(request,'register.html',context={'form':form})
            return res

        #* it is for again generated blank form for that      
        form=RegisterForm()
        res = render(request,'register.html',context={'form':form})
        return res




    