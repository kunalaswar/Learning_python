from django.shortcuts import render

from django.views.generic import View,TemplateView
from django.http import HttpResponse
# Create your views here.
class Helloworld(View): # this is predefiend class inherited by the Helloworld Class
    def get(self,request): #  it is a predefined method  it is we are override and get is the predefiend method 
        return HttpResponse('<h1> This  Response is from class based views</h1>')
    
#^ here we are using the render method 
class TemplateCBV(TemplateView): # here parent class will takecare everythings
     template_name = 'testapp/result.html'

# how to send context parameter 
class TemplateCBV2(TemplateView): #TemplateView is used only to display a template
    template_name = 'testapp/result2.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs) # here we calling parent method 
        context['name']='Sunny' #get_context_data() is used in Class-Based Views to pass dynamic data from the view to the template.
        context['marks']=98
        context['subject']='python'
        return context
        
# class TemplateCBV2(TemplateView):
#     # TemplateView is PREDEFINED class for displaying templates
    
#     template_name = 'testapp/result2.html'
#     # You're specifying which HTML template to show
    
#     def get_context_data(self, **kwargs):
#         # You're OVERRIDING the predefined get_context_data() method
#         # This method is used to SEND DATA to the template
#         # **kwargs = accepts any number of keyword arguments
        
#         context = super().get_context_data(**kwargs)
#         # super() = calling PARENT class (TemplateView) method
#         # You're getting the default context dictionary first
#         # context = {} (empty dictionary from parent)
        
#         context['name'] = 'Sunny'
#         # You're adding 'name' variable to context dictionary
#         # Now template can use {{ name }}
        
#         context['marks'] = 98
#         # You're adding 'marks' variable to context
#         # Now template can use {{ marks }}
        
#         context['subject'] = 'python'
#         # You're adding 'subject' variable to context
#         # Now template can use {{ subject }}
        
#         return context
#         # You're sending this dictionary to the template
#         # context = {'name': 'Sunny', 'marks': 98, 'subject': 'python'}


        

