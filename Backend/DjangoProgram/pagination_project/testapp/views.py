from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from testapp.models import Employee
from testapp.admin import EmployeeAdmin
from testapp.serializer import EmployeeSerializer
from rest_framework.pagination import PageNumberPagination
#   👉 This is Local pagination 
from testapp.pagination import MyPagination,MyPagination2,MyPagination3

# class EmployeeListView(generics.ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     # pagination_class  = MyPagination #we create this class upper see this 
#     #todo - if we comment this then Global setting is applicable 
#     # pagination_class  = MyPagination2 
#     pagination_class  = MyPagination3 
    

#todo - 9/6/2025 next vidoes seaching and filtering  

# class EmployeeListView(generics.ListAPIView):   # You are creating a class-based API view Its job is to: Handle GET requests Return a list of records    
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer # Converts Employee model objects →JSON
#     def get_queryset(self): # Which records should be returned for THIS request
#         qs = Employee.objects.all()
#         name = self.request.GET.get('ename') #Reads query parameter from URL
#         if name is not None: 
#             qs = qs.filter(ename__contains=name)
#             return qs 
#* after that if you want to run this project you have to put the http://127.0.0.1:8000/api/?ename=Nicole urls inside of this and search for it         
# http://127.0.0.1:8000/api/?ename=s 
#Execution flow: 
# URL hits EmployeeListView
# get_queryset() is called
# name = "jo"
# Filter applied
# Matching employees returned as JSON        

class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()   
    serializer_class = EmployeeSerializer
    # search_fields = ('eno',)#Why do we use a TUPLE here? Because SearchFilter expects a COLLECTION of fields, not just one field.
    # search_fields = ('^eno',) # Works only for CharField
    # search_fields = ('=eno',)
    # ordering_fields = ('ename',) # http://127.0.0.1:8000/api/?myordering=ename
    ordering_fields = ('eno','esal')   







        
        