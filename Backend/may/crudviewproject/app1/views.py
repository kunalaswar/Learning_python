from django.shortcuts import render
from django.views.generic import ListView ,UpdateView,DeleteView,CreateView,DetailView,TemplateView #this is predefined class
from app1.models import EmpModel
from django.urls import reverse_lazy
from app1.forms import EmpForm
from django.http import Http404,HttpResponse
# Create your views here.
class EmpListView(ListView):
    # model=EmpModel() we do not write paranthisis because we not create one recorded or object we can create all the record at a time 
    model = EmpModel #* you have to read the data from emp model 
    template_name  = 'emplist_temp.html'
    context_object_name = 'emp'

class EmpUpdateView(UpdateView): 
    model = EmpModel
    form_class = EmpForm
    template_name='empupdate_temp.html'
    # context_object_name='emp' #^ this is not required 
    success_url = reverse_lazy('listemp')

class EmpDeleteView(DeleteView): # this DeleteView is predefined Class present in generic module
    model = EmpModel #^ for deleting we dont required form_class
    template_name = 'empdelete_temp.html'
    success_url = reverse_lazy('listemp')
    context_object_name='emp' # emp is nothing but queryset and how executed a query GET method 

class EmpCreateView(CreateView):
    model = EmpModel
    template_name = "empcreate_temp.html"
    success_url = reverse_lazy('listemp')
    form_class = EmpForm

class EmpDetailsView(DetailView):
    model = EmpModel
    template_name = "empdetails_temp.html"
    context_object_name = "emp"
#*--------------------------------This is without handling Error ----------------------------------
class EmpListView1(ListView):
    model = EmpModel
    template_name = 'emplist_temp.html'
    context_object_name = 'emp '
    def get_queryset(self):
        # return super().get_queryset() # it return all the Employee details  But we want specifies details
        qs = self.model.objects.filter(job = 'hr') #this model is call with self or EmpListView1 classname #todo -first time i customise  value is given with in Queryset 
        return qs 
#*---------------------------------------------------------------------------------------------------
class EmpListView2(ListView):
    model = EmpModel
    template_name = 'emplist_temp.html'
    context_object_name = 'emp '
    def get_queryset(self):
        value = self.kwargs.get('job') #& here is a keyword argument kwargs
        qs = self.model.objects.filter(job = value)#todo -second time i customise  value is given with in captured parameter  
        return qs
#* video 40 16th jul    
class EmpListView3(ListView):
    model = EmpModel
    template_name = "emplist_temp.html"
    context_object_name="emp"
    def get_queryset(self): # you are try to override get_queryset() method
        # return super().get_queryset()
        job = self.request.GET.get('job')#& here is a request 
        qs = self.model.objects.filter(job=job)#todo -second time i customise  value is part of which one request 
        return qs

def joblist(request):
    res =  render(request,'empjob_temp.html',context={})
    return res 
#*--------------------------------This is with handling Error check it ----------------------------
class EmpDetailsView1(DetailView):
    model  = EmpModel
    template_name = "empdetails_temp.html"
    context_object_name="emp"
    def get(self,request,*vargs,**kwargs):
        #  it is called my get method of self class 
        try : # get method of super class is returining a response 
            res=super().get(request,vargs,kwargs)
            return res 
        except:
            # return HttpResponse("Invalid Emplolyee No ")
            res = render(request,"listemp")
            return res 


     # super class get method is not handling the Error    
    def get_object(self ):
        # return super().get_object(queryset)
        eno = self.kwargs.get('pk') # what is the name of captured parameter
        try: 
            obj = self.model.objects.get(empno = eno)
            return obj 
        except:
            raise Http404("Invalid EmployeeNo")#^Http404 is predefined Error Class that are present in django.httpimport Http404 
            # it is for raiseing the Error 

#*---------------------------------------------------------------------------------------------------
#! 17 july  Mixin class  
#todo - Upper code copy kela aahe Same 
class EmpDetailsMixin: # this  
      def get_object(self ):
        # return super().get_object(queryset)
        eno = self.kwargs.get('pk') # what is the name of captured parameter
        try: 
            obj = self.model.objects.get(empno = eno)
            return obj 
        except:
            raise Http404("Invalid EmployeeNo")#^Http404 is predefined Error Class that are present in django.httpimport Http404 
            # it is for raiseing the Error 

class EmpDetailsView4(EmpDetailsMixin,DetailView):
    model  = EmpModel
    template_name = "empdetails_temp.html"
    context_object_name="emp"
    def get(self,request,*vargs,**kwargs):
        #  it is called my get method of self class 
        try : # get method of super class is returining a response 
            res=super().get(request,vargs,kwargs)
            return res 
        except:
            # return HttpResponse("Invalid Emplolyee No ")
            res = render(request,"listemp")
            return res 
#^-------------------------------------------------------------        
# def joblist(request):
#     res =  render(request,'empjob_temp.html',context={})
#     return res  #^ this same code is return inside of TemplateView predefined class we only give the template_name
#^-------------------------------------------------------------        
class TestTempView(TemplateView): #^ This is Predefined class TemplateView class is inherited by TestTempView 
    template_name='test.html' # template_name is doing rendering the test.html and generated an response 

class TemplateMixin:
    msg = "Kunal Aswar "    
    def get_context_data(self,**kwargs):
        return super().get_context_data(msg=self.msg)

class TestTempView1(TemplateMixin,TemplateView):
    template_name="test.html"
    msg = "Python is Best"



