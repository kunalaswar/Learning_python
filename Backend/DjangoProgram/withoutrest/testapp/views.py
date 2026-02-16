from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def emp_data_view(request):
#     emp_data = {
#         'eno':101,
#         'ename':'sunny',
#         'esal':12000,
#         'eaddr':'mumbai'
#     }
#     resp = '<h1>Employee Number:{}<br>Employee Name:{}<br> Employee Salary:{}<br>Employee Address:{}</h1>' .format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'])
#     return HttpResponse(resp) 


    # import json
    # def emp_data_json_view(request):
    #     emp_data = {
    #         'eno':102,
    #         'ename':'sagar',
    #         'esal':11000,
    #         'eaddr':'vja'
    #     }
    #     json_data = json.dumps(emp_data)
    #     return  HttpResponse(json_data,content_type = 'application/json')




# 
# from django.http import JsonResponse
# from django.views.generic import View
# class JSONCBV(View):
#     def get(self,request,*args,**kwargs):
#         emp_data = {
#             'eno':101,
#             'ename':'katrina',
#             'esal':22000,
#             'eaddr':'Mumbai'           
#         }
#         return JsonResponse(emp_data)
          

#todo - CBV's  
import json
from django.http import HttpResponse
from django.views.generic import View
from django.http import JsonResponse

class JSONCBV(View):
    def get(self,request,*args,**kwargs):
        json_data = json.dumps({'msg':"this is from GET Method"})
        return HttpResponse(json_data,content_type = 'application/json') #^content_type =  The data I am sending is JSON 
    def post(self,request,*args,**kwargs):
        json_data = json.dumps({'msg':'This is from POST Method'})
        return HttpResponse(json_data,content_type='application/json')
    def put(self,request,*args,**kwargs):
        json_data = json.dumps({'msg':"this is from PUT Method "})
        return HttpResponse(json_data,content_type = 'application/json')
    
    def delete(self,request,*args,**kwargs):
        json_data = json.dumps({'msg':"this is from DELETE Method "})
        return HttpResponse(json_data,content_type = 'application/json')
    
    

