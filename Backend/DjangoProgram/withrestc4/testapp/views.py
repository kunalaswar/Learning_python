# from django.shortcuts import render
# from testapp.models import Employee
# from testapp.serializers import EmployeeSerializer
# from rest_framework.response import Response
# # from rest_framework.views import APIView
#todo
# from django.shortcuts import render
# from testapp.models import Employee
# from testapp.serializers import EmployeeSerializer
# from rest_framework.response import Response
# # from rest_framework.views import APIView
# from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
# # Create your views here.
# #? it is for getting the two method at a time 
# #todo - video 5/6/2025
# class EmployeeListCreateAPIView(ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer 

# class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer 
#     lookup_field = 'id'

# class EmployeeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer 
#     lookup_field = 'id' 

# class EmployeeRetrieveDestroyAPIView(RetrieveDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer 
#     lookup_field = 'id' 


#todo - Mixin class
from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
from rest_framework import mixins
#? 
#todo 
class EmployeeListCreateModelMixin(mixins.CreateModelMixin,ListAPIView):#!is called multiple inheritance.
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
class EmployeeRetrieveUpdateDestroyModelMixin(mixins.UpdateModelMixin,mixins.DestroyModelMixin,RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer 
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request, *args, **kwargs)
     
    def put(self,request,*args,**kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request, *args, **kwargs)
    

      