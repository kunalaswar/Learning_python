# from django.shortcuts import render
# from testapp.models import Employee
# from testapp.serializers import EmployeeSerializer
# from rest_framework.response import Response
# # from rest_framework.views import APIView
#todo- from rest_framework.generics import ListAPIView
# # Create your views here.
# class   EmployeeListAPIView(APIView):
#     def get(self,request,*args,**kwargs):
#         qs = Employee.objects.all() # to read all EMployee
#         serializer = EmployeeSerializer(qs,many=True) # serialization part 
#         return Response(serializer.data) # sending data 
    
from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView
# Create your views here.
# class EmployeeListAPIView(ListAPIView):
#     queryset = Employee.objects.all() 
#     serializer_class = EmployeeSerializer
        
# class EmployeeCreateAPIView(CreateAPIView):#^ CreateAPIView handles POST automatically
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer   

# class EmployeeRetrieveAPIView(RetrieveAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer 
#     lookup_field = 'id'
# 👉 EmployeeSerializer is a CLASS, not an object
# 👉 DRF wants the class, not an instance
# 👉 DRF itself creates the object at runtime    

# class EmployeeUpdateAPIView(UpdateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer 
#     lookup_field = 'id'

# #===========Delete===============
# class EmployeeDestroyAPIView(DestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer 
#     lookup_field = 'id'  

#todo - video 5/6/2025
class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer 
      
      